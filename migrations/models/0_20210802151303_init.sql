-- upgrade --
CREATE TABLE IF NOT EXISTS "baseforqueries" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "target_class" VARCHAR(100) NOT NULL,
    "data" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "genes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "gene_code" VARCHAR(50) NOT NULL,
    "comment" TEXT NOT NULL,
    "rs_code" VARCHAR(25) NOT NULL,
    "poly_type" VARCHAR(50) NOT NULL,
    "poly_status" VARCHAR(50) NOT NULL,
    "interpretation" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "people" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "lab_number" VARCHAR(10) NOT NULL UNIQUE,
    "name" VARCHAR(50) NOT NULL,
    "sex" VARCHAR(10) NOT NULL,
    "date_of_birth" VARCHAR(20) NOT NULL,
    "material_type" VARCHAR(50) NOT NULL,
    "date_of_analysis" VARCHAR(50) NOT NULL,
    "reason_of_analysis" TEXT NOT NULL,
    "comment" TEXT
);
CREATE TABLE IF NOT EXISTS "people_genes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "genes_id" INT NOT NULL REFERENCES "genes" ("id") ON DELETE CASCADE,
    "people_id" INT NOT NULL REFERENCES "people" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
