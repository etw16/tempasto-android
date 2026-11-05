package de.tempasto.app;

import android.os.Bundle;
import android.webkit.WebView;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        fixTextSize();
    }

    @Override
    public void onResume() {
        super.onResume();
        fixTextSize();
    }

    // Schriftgröße fest auf 100 %, damit das Layout auf jedem Handy gleich aussieht
    private void fixTextSize() {
        try {
            WebView wv = getBridge() != null ? getBridge().getWebView() : null;
            if (wv != null) {
                wv.getSettings().setTextZoom(100);
                // Tablets: die App skaliert sich über das viewport-Meta-Tag
                wv.getSettings().setUseWideViewPort(true);
                wv.getSettings().setLoadWithOverviewMode(true);
            }
        } catch (Exception ignored) { }
    }
}
