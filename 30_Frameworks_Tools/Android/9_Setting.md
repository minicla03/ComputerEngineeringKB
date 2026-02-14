**Settings UI**

Per costruire la UI delle impostazioni, si usano **sottoclassi della classe** Preference piuttosto che oggetti View. La classe Preference fornisce la View da visualizzare per ogni impostazione e si associa a un'interfaccia SharedPreferences per memorizzare/recuperare i dati.

Per visualizzare una lista di impostazioni, si usa una **Activity o un Fragment specializzato**. La best practice per Android 3.0+ è usare una SettingsActivity che ospita un PreferenceFragment. Per compatibilità con la v7 appcompat library, si estende la Settings Activity con AppCompatActivity e il fragment con PreferenceFragmentCompat. Per versioni più vecchie di Android (\<3.0), si usa PreferenceActivity. L'uso di PreferenceFragment è generalmente più flessibile rispetto alla sola PreferenceActivity.

Android Studio fornisce un **template Settings Activity**. Questo template facilita la creazione di schermate di impostazioni, specialmente se si hanno più gruppi di impostazioni. Fornisce layout diversi per smartphone (header links) e tablet (master/detail view). Il template crea i file XML (res/xml/) che definiscono le impostazioni (pref_data_sync.xml, pref_general.xml, pref_headers.xml, pref_notification.xml), risorse stringa (strings.xml), e le classi Activity/Fragment necessarie (SettingsActivity, AppCompatPreferenceActivity). Il template include anche la funzionalità per ascoltare i cambiamenti delle impostazioni e aggiornare il riassunto (summary).

La gerarchia delle impostazioni inizia con un layout PreferenceScreen.

# 1. Tipi di Controlli UI: Diverse sottoclassi di Preference offrono UI appropriate per modificare le impostazioni:

- CheckBoxPreference: Per impostazioni abilitate/disabilitate (valore booleano).
- ListPreference: Mostra una lista di pulsanti radio in un dialogo.
- SwitchPreference: Un'opzione toggle con due stati (on/off, true/false).
- EditTextPreference: Un campo di testo in un dialogo per l'inserimento di stringhe.
- RingtonePreference: Consente all'utente di scegliere una suoneria.

I valori delle impostazioni vengono memorizzati in un file **SharedPreferences**. Questo è un modo comune per persistere piccole quantità di dati primitivi come coppie chiave-valore tra le sessioni dell'app. Ogni oggetto Preference (impostazione) ha una coppia chiave-valore corrispondente che il sistema usa per salvare il valore in un file SharedPreferences predefinito.

Dopo aver salvato le impostazioni, è necessario **leggere i valori** dallo SharedPreferences file per usarli nella logica dell'app. Si può anche implementare un listener (Preference.OnPreferenceChangeListener) per reagire immediatamente ai cambiamenti di un'impostazione.

![The image is a simple MVVM-style diagram with three rectangular components and labeled arrows: - View (top-left) - ViewModel (below View) — contains an inner box labeled "State and Operations" - Model (right) Arrows and labels: - Solid arrow from View to ViewModel: "Data Binding and Commands" - Solid arrow from ViewModel to Model: "ViewModel updates the model" - Dashed curved arrow from ViewModel back to View: "Send Notifications" - Dashed curved arrow from Model back to ViewModel: "Send Notifications"](./Android_images/image_042.png)
