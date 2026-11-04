/* Tempasto: Brücke zu Android (Benachrichtigungen, Speichern/Teilen, Bildschirm an) */
(function(){
  var C=window.Capacitor, X=window.capacitorExports;
  if(!C||!C.isNativePlatform||!C.isNativePlatform()||!X)return;
  var reg=X.registerPlugin, LN=reg('LocalNotifications'), FS=reg('Filesystem'), SH=reg('Share'), KA=reg('KeepAwake'), AP=reg('App');
  var perm=null, tmr=null, last='';
  function b64(blob){return new Promise(function(res,rej){var r=new FileReader();r.onload=function(){res(String(r.result).split(',')[1]);};r.onerror=rej;r.readAsDataURL(blob);});}
  async function allowed(){
    if(perm!==null)return perm;
    try{var p=await LN.checkPermissions();if(p.display!=='granted')p=await LN.requestPermissions();perm=p.display==='granted';}catch(e){perm=false;}
    return perm;
  }
  async function sync(fn){
    var ev=[];try{ev=fn()||[];}catch(e){return;}
    var sig=JSON.stringify(ev);if(sig===last)return;last=sig;
    try{var pend=await LN.getPending();if(pend.notifications.length)await LN.cancel({notifications:pend.notifications.map(function(n){return {id:n.id};})});}catch(e){}
    if(!ev.length||!(await allowed()))return;
    var list=ev.slice(0,40).map(function(e,i){var n={id:1000+i,title:e.title,body:e.body,largeBody:e.body,schedule:{at:new Date(e.at),allowWhileIdle:true},channelId:CH,smallIcon:'ic_stat_tempasto',iconColor:'#C2281B',sound:'gong.wav'};if(e.sid){n.actionTypeId='step';n.extra={sid:e.sid};}return n;});
    try{await LN.schedule({notifications:list});}catch(e){last='';}
  }
  window.TEMPASTO_NATIVE={
    shareText:async function(t){if(!SH)return false;try{await SH.share({text:t,dialogTitle:'Plan teilen'});}catch(e){if(!/cancel/i.test((e&&e.message)||''))return false;}return true;},
    save:async function(name,blob){
      try{var r=await FS.writeFile({path:name,data:await b64(blob),directory:'CACHE'});
        await SH.share({title:name,files:[r.uri],dialogTitle:'Speichern oder teilen'});}
      catch(e){if(!/cancel/i.test((e&&e.message)||'')){try{toast('Das hat nicht geklappt');}catch(_){}}}
      return true;
    },
    plan:function(fn){clearTimeout(tmr);tmr=setTimeout(function(){sync(fn);},800);},
    wake:function(on){try{on?KA.keepAwake():KA.allowSleep();}catch(e){}}
  };
  var CH='tempasto-gong';
  LN.createChannel({id:CH,name:'Backplan',description:'Erinnerungen an die Teigschritte',importance:5,visibility:1,vibration:true,sound:'gong.wav'}).catch(function(){});
  LN.registerActionTypes({types:[{id:'step',actions:[{id:'done',title:'Erledigt'},{id:'later',title:'+10 Min'}]}]}).catch(function(){});
  window.addEventListener('load',function(){
    if(window.TEMPASTO_APP)TEMPASTO_NATIVE.plan(TEMPASTO_APP.notifEvents);
    if(!('speechSynthesis' in window)){var v=document.getElementById('ckVoice');if(v)v.hidden=true;}
  });
  // Zurück-Taste: erst Fenster schließen, dann Backmodus, dann zur Startseite
  // Tipp auf eine Erinnerung öffnet direkt den Backmodus
  LN.addListener('localNotificationActionPerformed',function(r){var A=window.TEMPASTO_APP;if(!A)return;var sid=r&&r.notification&&r.notification.extra&&r.notification.extra.sid;
    setTimeout(function(){if(r&&r.actionId==='done'&&sid)A.stepDone(sid);else if(r&&r.actionId==='later'&&sid)A.snooze(sid);else A.openCook();},300);});
  AP.addListener('backButton',function(){var A=window.TEMPASTO_APP;try{if(A&&A.back())return;}catch(e){}AP.minimizeApp();});
  document.addEventListener('visibilitychange',function(){if(!document.hidden&&window.TEMPASTO_APP){last='';TEMPASTO_NATIVE.plan(TEMPASTO_APP.notifEvents);}});
})();
