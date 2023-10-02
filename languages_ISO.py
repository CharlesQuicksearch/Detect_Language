import numpy as np

language_codes = np.array(
        [("Arabic", "ar-sa", "ar"),
         ("English", 'en-AU', 'en-US'),
         ("English", 'en-GB', 'en'),
         ("Swedish", 'sv-SE', 'sv'),
         ("Catalan", "ca-ES", "ca"),
         ("Chinese", "zh-CN", "zh"),
         ("Chinese", "zh-Hant", "zh"),
         ("Czech", "cs-CZ", "cz"),
         ("Dutch", "nl-BE", "nl"), #nl added not in list
         ("Estonian", "et-EE", "et"),
         ("French", "fr-FR", "fr"),
         ("German", "de-AT", "de"),
         ("Greek", "el-GR", "el"),
         ("Indonesian", "id", "id"),
         ("Italian", "it-IT", "it"),
         ("Japanese", "ja-JP", "ja"),
         ("Latvian", "lv-LV", "lv"),
         ("Polish", "pl-PL", "pl"),
         ("Portuguese", "pt-PT", "pt"),
         ("Romanian", "ro-RO", "ro"),
         ("Russian", "ru-RU", "ru"),
         ("Ukrainian", "uk", "uk"), #Ukrainian
         ("Spanish", "es-ES", "es"),
         ("Turkish", "tr-TR", "tr"),
         ("Welsh", "unknown", "cy")],
        dtype=[('id', 'U10'), ('code1', 'U10'), ('code2', 'U10')])
