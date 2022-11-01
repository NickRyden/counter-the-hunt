BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "whitelist" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"mac_addr"	TEXT,
	"friendly_name"	INTEGER
);
CREATE TABLE IF NOT EXISTS "hashes" (
	"id"	TEXT UNIQUE,
	"md5"	TEXT,
	"sha256"	TEXT,
	PRIMARY KEY("md5")
);
CREATE TABLE IF NOT EXISTS "forensics" (
	"id"	TEXT,
	"mac_addr"	TEXT UNIQUE,
	"time_followed"	TEXT,
	"first_time"	TEXT,
	"last_time"	TEXT,
	"details"	TEXT,
	PRIMARY KEY("mac_addr")
);
CREATE TABLE IF NOT EXISTS "devices" (
	"first_time"	INTEGER,
	"last_time"	INTEGER,
	"mac_addr"	TEXT,
	"freq"	INTEGER,
	"crypt"	TEXT,
	"manufacturer"	TEXT,
	"device_type"	TEXT,
	"sssid"	TEXT,
	"bssid"	TEXT
);
COMMIT;
