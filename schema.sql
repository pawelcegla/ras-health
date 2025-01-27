CREATE TABLE ras_health_log (local_timestamp TEXT NOT NULL UNIQUE DEFAULT (strftime('%FT%T+00:00', 'now', 'utc')), ras_timestamp TEXT NOT NULL UNIQUE);
