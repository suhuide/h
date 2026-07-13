```c
diff --git a/app/app_colorlight_mgr.cpp b/app/app_colorlight_mgr.cpp
index 12c7424..8c005a4 100644
--- a/app/app_colorlight_mgr.cpp
+++ b/app/app_colorlight_mgr.cpp
@@ -202,6 +202,18 @@ void AppColorLightDev::SetCurrentLevel(uint8_t current_level)
         current_level = 1;
     }

+    // The reported level may have precision loss due to the *254/DLML conversion.
+    // If the difference is ≤1, skip the report to avoid overwriting the accurate value in the attribute.
+    {
+        uint8_t cur_level = 0;
+        LevelControl::Attributes::CurrentLevel::Get(m_ep, &cur_level);
+        int16_t diff = std::abs((int16_t)current_level - (int16_t)cur_level);
+        if (diff <= 1) {
+            LOG_MSG_INFO(TAG_LIT, "EP[%u] CurrentLevel unchanged (diff %d), skip\n", m_ep, diff);
+            return;
+        }
+    }
+
     LOG_MSG_INFO(TAG_LIT, "EP[%u] set CurrentLevel %u\n", m_ep, current_level);

     PlatformMgr().LockChipStack();
```