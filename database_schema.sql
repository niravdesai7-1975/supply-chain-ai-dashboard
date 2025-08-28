-- Supply Chain AI Use Cases Database Schema
-- This schema organizes AI use cases for supply chain and procurement operations

-- Sectors table
CREATE TABLE sectors (
    sector_id SERIAL PRIMARY KEY,
    sector_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Value chains table
CREATE TABLE value_chains (
    value_chain_id SERIAL PRIMARY KEY,
    value_chain_name VARCHAR(200) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Use case categories table
CREATE TABLE use_case_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(150) NOT NULL UNIQUE,
    description TEXT,
    business_impact_rating INTEGER CHECK (business_impact_rating BETWEEN 1 AND 5),
    implementation_complexity INTEGER CHECK (implementation_complexity BETWEEN 1 AND 5),
    estimated_roi_percentage DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Personas table
CREATE TABLE personas (
    persona_id SERIAL PRIMARY KEY,
    persona_name VARCHAR(150) NOT NULL UNIQUE,
    role_description TEXT,
    department VARCHAR(100),
    decision_making_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI technologies table
CREATE TABLE ai_technologies (
    technology_id SERIAL PRIMARY KEY,
    technology_name VARCHAR(100) NOT NULL UNIQUE,
    technology_type VARCHAR(50),
    description TEXT,
    maturity_level VARCHAR(20),
    vendor_ecosystem TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Main use cases table
CREATE TABLE use_cases (
    use_case_id SERIAL PRIMARY KEY,
    use_case_name VARCHAR(200) NOT NULL,
    sector_id INTEGER REFERENCES sectors(sector_id),
    value_chain_id INTEGER REFERENCES value_chains(value_chain_id),
    category_id INTEGER REFERENCES use_case_categories(category_id),
    persona_id INTEGER REFERENCES personas(persona_id),
    description TEXT NOT NULL,
    business_objective TEXT,
    key_benefits TEXT,
    success_metrics TEXT,
    implementation_timeline_months INTEGER,
    estimated_budget_range VARCHAR(50),
    risk_level VARCHAR(20),
    priority_score DECIMAL(3,2),
    status VARCHAR(20) DEFAULT 'Proposed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_use_cases_sector ON use_cases(sector_id);
CREATE INDEX idx_use_cases_category ON use_cases(category_id);
CREATE INDEX idx_use_cases_priority ON use_cases(priority_score DESC);
CREATE INDEX idx_use_cases_status ON use_cases(status);
