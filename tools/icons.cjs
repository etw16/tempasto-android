// Rendert App-Symbole und Startbild aus dem Tempasto-Logo: node tools/icons.cjs
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
const fs=require('fs'),path=require('path');const R=path.join(__dirname,'..','android','app','src','main','res');
const PZ=fs.readFileSync(path.join(__dirname,'..','..','tempasto','icon.svg'),'utf8').match(/<g transform[^>]*>([\s\S]*?)<\/g>/)[1];
const pizza=(cx,cy,d)=>`<g transform="translate(${cx} ${cy}) scale(${d/24}) translate(-12 -12)">${PZ}</g>`;
const svg=(w,h,body,bg='')=>`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${bg}${body}</svg>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage();
async function png(s,w,h,out){await p.setViewportSize({width:w,height:h});await p.setContent(`<style>*{margin:0}body{background:transparent}</style>${s}`);await p.screenshot({path:out,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});}
const D={mdpi:1,hdpi:1.5,xhdpi:2,xxhdpi:3,xxxhdpi:4};
for(const [k,f] of Object.entries(D)){const L=48*f,F=108*f;
 await png(svg(L,L,pizza(L/2,L/2,L*.76),`<rect width="${L}" height="${L}" rx="${L*.22}" fill="#C2281B"/>`),L,L,`${R}/mipmap-${k}/ic_launcher.png`);
 await png(svg(L,L,pizza(L/2,L/2,L*.74),`<circle cx="${L/2}" cy="${L/2}" r="${L/2}" fill="#C2281B"/>`),L,L,`${R}/mipmap-${k}/ic_launcher_round.png`);
 await png(svg(F,F,pizza(F/2,F/2,F*.56)),F,F,`${R}/mipmap-${k}/ic_launcher_foreground.png`);}
const sp=(w,h)=>{const d=Math.min(w,h)*.28;return svg(w,h,pizza(w/2,h/2-d*.15,d)+`<text x="${w/2}" y="${h/2+d*.75}" text-anchor="middle" font-family="sans-serif" font-weight="800" font-size="${d*.32}" fill="#1E1C1A">Impasto</text>`,`<rect width="${w}" height="${h}" fill="#F3F4EF"/>`);};
for(const f of fs.readdirSync(R).filter(x=>x.startsWith('drawable'))){const fp=`${R}/${f}/splash.png`;if(!fs.existsSync(fp))continue;
 const m=/land/.test(f),s={mdpi:[320,480],hdpi:[480,800],xhdpi:[720,1280],xxhdpi:[960,1600],xxxhdpi:[1280,1920]}[(f.split('-').pop())]||[320,480];
 const [w,h]=f==='drawable'?[480,320]:(m?[s[1],s[0]]:s);await png(sp(w,h),w,h,fp);}
await b.close();console.log('ok');})();
