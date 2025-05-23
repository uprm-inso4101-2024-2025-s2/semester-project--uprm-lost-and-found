
-- Check if tables exist before creating them
DROP TABLE IF EXISTS ClaimItems;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS FoundItems;
DROP TABLE IF EXISTS Comments;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS LostItems;
DROP TABLE IF EXISTS Users;

USE LostAndFoundDatabase

-- Tabla de los users
CREATE TABLE Users (
    U_ID INT AUTO_INCREMENT PRIMARY KEY,
    U_Username VARCHAR(20) NOT NULL,
    U_Fullname VARCHAR(100) NOT NULL,
    U_Email VARCHAR(30) NOT NULL,
    U_Password VARCHAR(20) NOT NULL,
    U_Occupation VARCHAR(30) NOT NULL,
    U_ProfilePhoto LONGBLOB
);



-- Tabla de Objetos Perdidos
CREATE TABLE LostItems (
    L_ID INT AUTO_INCREMENT PRIMARY KEY,
    L_Description VARCHAR(120) NOT NULL,
    L_PublishDate DATE NOT NULL,
    L_Photo LONGBLOB,
    L_Information VARCHAR(500),
    L_Location VARCHAR(120) NOT NULL,
    L_Email VARCHAR(30) NOT NULL,
    U_ID INT NOT NULL,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID) ON DELETE CASCADE
);

-- Tabla de Ubicaciones
CREATE TABLE Location (
    P_ID INT AUTO_INCREMENT PRIMARY KEY,
    P_Name VARCHAR(20) NOT NULL,
    P_Coordinates VARCHAR(30) NOT NULL
);

-- Tabla de Comentarios
CREATE TABLE Comments (
    C_ID INT AUTO_INCREMENT PRIMARY KEY,
    C_Content VARCHAR(500) NOT NULL,
    C_PublishDate DATE NOT NULL,
    U_ID INT NOT NULL,
    L_ID INT NOT NULL,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID) ON DELETE CASCADE,
    FOREIGN KEY (L_ID) REFERENCES LostItems(L_ID) ON DELETE CASCADE
);

-- Tabla de Objetos Encontrados
CREATE TABLE FoundItems (
    F_ID INT AUTO_INCREMENT PRIMARY KEY,
    F_Photo LONGBLOB,
    F_Description VARCHAR(12) NOT NULL,
    F_Email VARCHAR(30) NOT NULL,
    F_PublishDate VARCHAR(10) NOT NULL,
    F_PlaceFound VARCHAR(120) NOT NULL,
    F_AdditionalDetails VARCHAR(500),
    U_ID INT NOT NULL,
    P_ID INT NULL,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID) ON DELETE CASCADE,
    FOREIGN KEY (P_ID) REFERENCES Location(P_ID) ON DELETE CASCADE  -- Removed for now, add back if needed and Location table exists
);

-- Tabla de Matches
CREATE TABLE Matches (
    M_ID INT AUTO_INCREMENT PRIMARY KEY,
    M_LostItemID INT NOT NULL,
    M_FoundItemID INT NOT NULL,
    M_MatchScore FLOAT NOT NULL,
    M_DateMatched TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    M_Status ENUM('pending', 'confirmed', 'rejected') DEFAULT 'pending',
    FOREIGN KEY (M_LostItemID) REFERENCES LostItems(L_ID) ON DELETE CASCADE,
    FOREIGN KEY (M_FoundItemID) REFERENCES FoundItems(F_ID) ON DELETE CASCADE
);


-- Tabla de Claim Items
CREATE TABLE ClaimItems(
	CR_ID INT  AUTO_INCREMENT PRIMARY KEY,
	F_ID INT NOT NULL,
	U_ID INT NOT NULL,
	CR_STATUS ENUM('pending', 'claimed', 'declined') DEFAULT 'pending',
    FOREIGN KEY (F_ID) REFERENCES FoundItems(F_ID) ON DELETE CASCADE,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID) ON DELETE CASCADE
);