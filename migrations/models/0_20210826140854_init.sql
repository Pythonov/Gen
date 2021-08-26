-- upgrade --
CREATE TABLE IF NOT EXISTS "genes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "gene_code" VARCHAR(50) NOT NULL,
    "rs_code" VARCHAR(25) NOT NULL,
    "poly_type" VARCHAR(50) NOT NULL,
    "poly_status" VARCHAR(50) NOT NULL,
    "interpretation" TEXT NOT NULL,
    "protein" TEXT NOT NULL,
    "comment" TEXT NOT NULL,
    CONSTRAINT "uid_genes_rs_code_0a5616" UNIQUE ("rs_code", "gene_code", "poly_type")
);
CREATE TABLE IF NOT EXISTS "people" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "lab_number" VARCHAR(10) NOT NULL UNIQUE,
    "name" VARCHAR(50) NOT NULL,
    "sex" VARCHAR(10) NOT NULL,
    "date_of_birth" VARCHAR(20) NOT NULL,
    "material_type" VARCHAR(50) NOT NULL,
    "date_of_analysis" VARCHAR(50) NOT NULL,
    "reason_of_analysis" TEXT NOT NULL,
    "comment" TEXT
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "genes_people" (
    "genes_id" INT NOT NULL REFERENCES "genes" ("id") ON DELETE CASCADE,
    "people_id" INT NOT NULL REFERENCES "people" ("id") ON DELETE CASCADE
);
