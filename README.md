# sale_ext – Sale and Account Customization

Odoo-**18.0**-Addon für die **Herr Informatik GmbH**. Das Modul ersetzt die Standard-PDFs von Odoo durch deutsch-/schweizlokalisierte Layouts für **Offerten / Auftragsbestätigungen** und **Kundenrechnungen** und ergänzt ein kleines Feld am Verkaufsauftrag.

## Funktionsumfang

- **Eigene Offerten-/Auftragsbestätigungs-PDF** (`report_saleorder_new`) – eigenständiger QWeb-Report, als Druckaktion am `sale.order` registriert. Überschrift abhängig vom Status: `draft`/`sent` → «Offerte», sonst → «Auftragsbestätigung».
- **Angepasste Rechnungs-PDF** – erbt und überschreibt `account.report_invoice_document` sowie die Steuersummen-Vorlage (Zwischensumme / Gesamtbetrag).
- **Eigener Seitenrahmen** – Header (Firmenlogo) und Footer (Adressblock, Telefon, Seitenzahlen, AGB-Link) über `web.external_layout_standard`.
- **Feld `title`** am `sale.order`, das in der Offerten-Überschrift gedruckt wird.

Gemeinsame Tabellenstruktur beider Dokumente: `Pos. | Artikel Nr. | Bezeichnung | Menge | Einzelpreis | Rabatt | Netto/Gesamt`, mit separater Beschreibungszeile (inkl. optionalem Produktbild) und Zwischensummen je Abschnitt.

## Installation

Das Verzeichnis `sale_ext/` in den Addons-Pfad der Odoo-Instanz legen und das Modul installieren/aktualisieren:

```bash
odoo -u sale_ext -d <datenbank>
```

Alternativ über die Apps-Oberfläche («Aktualisieren»). QWeb-Report-Änderungen werden mit dem Modul-Upgrade wirksam.

## Abhängigkeiten

`base`, `sale`, `account`, `sale_management`

## Struktur

```
sale_ext/
├── __manifest__.py              # Modul-Definition, Ladereihenfolge der data-Dateien
├── models/sale_order.py         # Feld "title" am sale.order
├── views/sale_order_view.xml    # Feld "title" im Auftragsformular
├── report/
│   ├── web_layout.xml           # Header/Footer (externes Layout)
│   ├── sale_order_templates.xml # Offerten-/Auftragsbestätigungs-PDF
│   ├── invoice_report_templates.xml  # Rechnungs-PDF (Vererbung)
│   └── ir_actions_report.xml    # Druckaktion für den Offerten-Report
└── security/ir.model.access.csv # nur Header (keine neuen Modelle)
```

## Hinweise

- Alle kundenseitigen Texte sind **deutsch (Schweiz)**: MWSt, Bearbeiter, Gültigkeitsdatum, Zwischensumme, Gesamtbetrag.
- Der Offerten-Report druckt `doc.title` (in diesem Modul definiert). Die Rechnung druckt `o.x_studio_titel` – ein **Odoo-Studio-Feld an `account.move`, das nicht in diesem Repo definiert ist**.
- Firmenangaben (Adresse, Telefon, AGB-URL `https://erp.rzcloud.ch/terms`) sind in `web_layout.xml`, `sale_order_templates.xml` und `invoice_report_templates.xml` **dupliziert** – bei Änderungen alle drei anpassen.

## Lizenz

AGPL-3
