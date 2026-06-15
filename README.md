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

## Deployment / Server

Die Applikation läuft on-premise auf dem Linux-Server **`srvodoov06`** (Odoo 18, `.deb`-Installation).

| Was | Pfad / Wert |
|-----|-------------|
| Live-Instanz | `https://erp.rzcloud.ch` |
| Odoo-Config | `/etc/odoo/odoo.conf` (kein expliziter `addons_path` → Default) |
| Modul auf dem Server | `/usr/lib/python3/dist-packages/odoo/addons/sale_ext` |
| Besitzer der Modul-Dateien | `manager:manager` |
| systemd-Dienst | `odoo` (`systemctl restart odoo`) |

> **Achtung:** Das Modul liegt im Core-Addons-Verzeichnis des Odoo-`.deb`-Pakets. Ein `apt`-Update von Odoo kann diesen Ordner überschreiben. Das Repo wurde dort historisch direkt über das Core-Verzeichnis geklont (verwaistes `.git` in `.../odoo/addons`) — Updates daher **nicht** per `git pull` an Ort und Stelle, sondern wie unten beschrieben.

### Update einspielen

```bash
# 1. Repo frisch in temp-Ordner klonen
git clone https://github.com/JosipFX/odoo-sale-template.git /tmp/sale_ext_update

# 2. Nur das Modul ersetzen
cd /usr/lib/python3/dist-packages/odoo/addons
rm -rf sale_ext
cp -r /tmp/sale_ext_update/sale_ext ./sale_ext
chown -R manager:manager sale_ext
rm -rf /tmp/sale_ext_update

# 3. Dienst neu starten
systemctl restart odoo
```

Danach im UI: **Apps → „sale_ext" → ⋮ → Aktualisieren** (lädt die geänderten QWeb-Reports in die DB). Ein reiner Restart genügt für Report-Änderungen **nicht**.

## Lizenz

AGPL-3
