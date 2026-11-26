```c
diff --git a/app/app_colorlight_mgr.cpp b/app/app_colorlight_mgr.cpp
index a230acb..12c7424 100644
--- a/app/app_colorlight_mgr.cpp
+++ b/app/app_colorlight_mgr.cpp
@@ -286,6 +286,16 @@ void AppColorLightDev::SetXYFromRGB(uint8_t red, uint8_t green, uint8_t blue)
         return;
     }

+    // Skip updating CurrentX/Y when device is OFF
+    {
+        bool onoff = false;
+        OnOff::Attributes::OnOff::Get(m_ep, &onoff);
+        if (!onoff) {
+            LOG_MSG_INFO(TAG_LIT, "EP[%u] device is OFF, skip XY update from HW report\n", m_ep);
+            return;
+        }
+    }
+
     RgbColor_t rgb;
     rgb.r = red;
     rgb.g = green;
```