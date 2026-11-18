
USE master;
GO

IF DB_ID('RetailAnalyticsDW') IS NULL
    CREATE DATABASE RetailAnalyticsDW;
GO

USE RetailAnalyticsDW;
GO

CREATE SCHEMA src;
GO
CREATE SCHEMA stg;
GO
CREATE SCHEMA dim;
GO
CREATE SCHEMA fact;
GO


USE RetailAnalyticsDW;
GO

CREATE TABLE src.Customers
(
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(150),
    City VARCHAR(100) NOT NULL
);

CREATE TABLE src.Products
(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    UnitPrice DECIMAL(12,2) NOT NULL
);

CREATE TABLE src.Sales
(
    SalesID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ProductID INT NOT NULL,
    StoreID INT NOT NULL,
    SalesDate DATE NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_SourceSales_Customer
        FOREIGN KEY (CustomerID)
        REFERENCES src.Customers(CustomerID),

    CONSTRAINT FK_SourceSales_Product
        FOREIGN KEY (ProductID)
        REFERENCES src.Products(ProductID),

    CONSTRAINT CK_SourceSales_Quantity
        CHECK (Quantity > 0)
);
GO


INSERT INTO src.Customers
(CustomerID, CustomerName, Email, City)
VALUES
(101, 'Rahul Sharma', 'rahul@gmail.com', 'Mumbai'),
(102, 'Priya Patel', 'priya@gmail.com', 'Ahmedabad'),
(103, 'Amit Shah', 'amit@gmail.com', 'Pune'),
(104, 'Neha Mehta', 'neha@gmail.com', 'Mumbai'),
(105, 'Karan Desai', 'karan@gmail.com', 'Surat');
GO
SELECT * FROM src.Customers;
GO

INSERT INTO src.Products
(ProductID, ProductName, Category, UnitPrice)
VALUES
(201, 'Laptop', 'Electronics', 55000),
(202, 'Mobile', 'Electronics', 25000),
(203, 'Office Chair', 'Furniture', 8000),
(204, 'Desk', 'Furniture', 12000),
(205, 'Headphones', 'Accessories', 3000);
GO
SELECT * FROM src.Products;
GO

INSERT INTO src.Sales
(SalesID, CustomerID, ProductID,
 StoreID, SalesDate, Quantity, UnitPrice)
VALUES
(1,101,201,1,'2025-01-10',1,55000),
(2,102,202,2,'2025-01-15',2,25000),
(3,103,203,3,'2025-02-05',3,8000),
(4,104,204,1,'2025-02-20',1,12000),
(5,105,205,2,'2025-03-10',4,3000),
(6,101,202,1,'2025-04-15',1,25000),
(7,102,201,2,'2025-05-12',1,55000),
(8,103,205,3,'2025-06-18',2,3000),
(9,104,203,1,'2025-07-05',2,8000),
(10,105,204,2,'2025-08-22',1,12000);
GO
SELECT * FROM src.Sales;
GO

SELECT
    s.SalesID,
    s.SalesDate,
    c.CustomerName,
    p.ProductName,
    p.Category,
    s.Quantity,
    s.UnitPrice,
    s.Quantity * s.UnitPrice AS SalesAmount
FROM src.Sales s
INNER JOIN src.Customers c
    ON s.CustomerID = c.CustomerID
INNER JOIN src.Products p
    ON s.ProductID = p.ProductID
ORDER BY s.SalesDate;
GO


SELECT
    SUM(Quantity * UnitPrice) AS TotalRevenue,
    SUM(Quantity) AS TotalUnitsSold,
    COUNT(*) AS TotalSalesTransactions
FROM src.Sales;
GO

SELECT
    p.Category,
    SUM(s.Quantity * s.UnitPrice) AS Revenue
FROM src.Sales s
JOIN src.Products p
    ON s.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Revenue DESC;
GO

SELECT
    YEAR(SalesDate) AS SalesYear,
    MONTH(SalesDate) AS SalesMonth,
    SUM(Quantity * UnitPrice) AS Revenue
FROM src.Sales
GROUP BY
    YEAR(SalesDate),
    MONTH(SalesDate)
ORDER BY SalesYear, SalesMonth;
GO

SELECT TOP 3
    c.CustomerID,
    c.CustomerName,
    SUM(s.Quantity * s.UnitPrice) AS Revenue
FROM src.Sales s
JOIN src.Customers c
    ON s.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.CustomerName
ORDER BY Revenue DESC, c.CustomerID;
GO


CREATE TABLE dim.DimDate
(
    DateKey INT PRIMARY KEY,
    FullDate DATE NOT NULL UNIQUE,
    DayNumber INT NOT NULL,
    MonthNumber INT NOT NULL,
    MonthName VARCHAR(20) NOT NULL,
    QuarterNumber INT NOT NULL,
    YearNumber INT NOT NULL
);
GO


CREATE TABLE dim.DimProduct
(
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL UNIQUE,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    UnitPrice DECIMAL(12,2) NOT NULL
);
GO

CREATE TABLE dim.DimStore
(
    StoreKey INT IDENTITY(1,1) PRIMARY KEY,
    StoreID INT NOT NULL UNIQUE,
    StoreName VARCHAR(100) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Region VARCHAR(100) NOT NULL
);
GO


CREATE TABLE dim.DimCustomer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(150),
    City VARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    IsCurrent BIT NOT NULL,

    CONSTRAINT CK_DimCustomer_Dates
        CHECK (StartDate < EndDate)
);
GO

CREATE UNIQUE INDEX UX_DimCustomer_Version
ON dim.DimCustomer(CustomerID, StartDate);

CREATE UNIQUE INDEX UX_DimCustomer_Current
ON dim.DimCustomer(CustomerID)
WHERE IsCurrent = 1;
GO


CREATE TABLE fact.FactSales
(
    SalesKey BIGINT IDENTITY(1,1) PRIMARY KEY,
    SalesID INT NOT NULL UNIQUE,
    DateKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    ProductKey INT NOT NULL,
    StoreKey INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(12,2) NOT NULL,
    SalesAmount DECIMAL(14,2) NOT NULL,

    CONSTRAINT FK_FactSales_Date
        FOREIGN KEY (DateKey)
        REFERENCES dim.DimDate(DateKey),

    CONSTRAINT FK_FactSales_Customer
        FOREIGN KEY (CustomerKey)
        REFERENCES dim.DimCustomer(CustomerKey),

    CONSTRAINT FK_FactSales_Product
        FOREIGN KEY (ProductKey)
        REFERENCES dim.DimProduct(ProductKey),

    CONSTRAINT FK_FactSales_Store
        FOREIGN KEY (StoreKey)
        REFERENCES dim.DimStore(StoreKey),

    CONSTRAINT CK_FactSales_Quantity
        CHECK (Quantity > 0)
);
GO

DECLARE @StartDate DATE = '2025-01-01';
DECLARE @EndDate DATE = '2026-12-31';

;WITH Dates AS
(
    SELECT @StartDate AS FullDate

    UNION ALL

    SELECT DATEADD(DAY, 1, FullDate)
    FROM Dates
    WHERE FullDate < @EndDate
)
INSERT INTO dim.DimDate
(
    DateKey,
    FullDate,
    DayNumber,
    MonthNumber,
    MonthName,
    QuarterNumber,
    YearNumber
)
SELECT
    YEAR(FullDate) * 10000
        + MONTH(FullDate) * 100
        + DAY(FullDate),
    FullDate,
    DAY(FullDate),
    MONTH(FullDate),
    DATENAME(MONTH, FullDate),
    DATEPART(QUARTER, FullDate),
    YEAR(FullDate)
FROM Dates
OPTION (MAXRECURSION 0);
GO

SELECT * FROM dim.DimDate;
GO

INSERT INTO dim.DimProduct
(
    ProductID,
    ProductName,
    Category,
    UnitPrice
)
SELECT
    ProductID,
    ProductName,
    Category,
    UnitPrice
FROM src.Products;
GO
SELECT * FROM dim.DimProduct;
GO

INSERT INTO dim.DimStore
(StoreID, StoreName, City, Region)
VALUES
(1, 'Mumbai Central', 'Mumbai', 'West'),
(2, 'Ahmedabad Mall', 'Ahmedabad', 'West'),
(3, 'Pune Outlet', 'Pune', 'West');
GO
SELECT * FROM dim.DimStore;
GO

INSERT INTO dim.DimCustomer
(
    CustomerID,
    CustomerName,
    Email,
    City,
    StartDate,
    EndDate,
    IsCurrent
)
SELECT
    CustomerID,
    CustomerName,
    Email,
    City,
    '2025-01-01',
    '9999-12-31',
    1
FROM src.Customers;
GO
SELECT * FROM dim.DimCustomer;
GO

INSERT INTO fact.FactSales
(
    SalesID,
    DateKey,
    CustomerKey,
    ProductKey,
    StoreKey,
    Quantity,
    UnitPrice,
    SalesAmount
)
SELECT
    s.SalesID,
    d.DateKey,
    c.CustomerKey,
    p.ProductKey,
    st.StoreKey,
    s.Quantity,
    s.UnitPrice,
    s.Quantity * s.UnitPrice
FROM src.Sales s

INNER JOIN dim.DimDate d
    ON s.SalesDate = d.FullDate

INNER JOIN dim.DimCustomer c
    ON s.CustomerID = c.CustomerID
   AND s.SalesDate >= c.StartDate
   AND s.SalesDate < c.EndDate

INNER JOIN dim.DimProduct p
    ON s.ProductID = p.ProductID

INNER JOIN dim.DimStore st
    ON s.StoreID = st.StoreID;
GO
SELECT * FROM fact.FactSales;
GO

SELECT
    COUNT(*) AS FactRows,
    SUM(Quantity) AS TotalQuantity,
    SUM(SalesAmount) AS TotalRevenue
FROM fact.FactSales;
GO

-- Implement SCD

CREATE TABLE stg.CustomerStage
(
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(150),
    City VARCHAR(100) NOT NULL
);
GO

INSERT INTO stg.CustomerStage
(
    CustomerID,
    CustomerName,
    Email,
    City
)
SELECT
    CustomerID,
    CustomerName,
    Email,
    City
FROM src.Customers;
GO

SELECT * FROM stg.CustomerStage;
GO

--Implement SCD Type 1

UPDATE src.Customers
SET Email = 'rahul.sharma@gmail.com'
WHERE CustomerID = 101;
GO
SELECT * FROM src.Customers;
GO
SELECT * FROM stg.CustomerStage;
GO

TRUNCATE TABLE stg.CustomerStage;

INSERT INTO stg.CustomerStage
(
    CustomerID,
    CustomerName,
    Email,
    City
)
SELECT
    CustomerID,
    CustomerName,
    Email,
    City
FROM src.Customers;
GO


SELECT
    d.CustomerID,
    d.CustomerName,
    d.Email AS OldEmail,
    s.Email AS NewEmail
FROM dim.DimCustomer d
JOIN stg.CustomerStage s
    ON d.CustomerID = s.CustomerID
WHERE d.IsCurrent = 1
  AND
  (
      ISNULL(d.Email, '') <>
          ISNULL(s.Email, '')
      OR d.CustomerName <> s.CustomerName
  );
GO

UPDATE d
SET
    d.CustomerName = s.CustomerName,
    d.Email = s.Email
FROM dim.DimCustomer d
JOIN stg.CustomerStage s
    ON d.CustomerID = s.CustomerID
WHERE
    d.CustomerName <> s.CustomerName
    OR ISNULL(d.Email, '') <>
       ISNULL(s.Email, '');
GO

SELECT
    CustomerKey,
    CustomerID,
    CustomerName,
    Email,
    City,
    IsCurrent
FROM dim.DimCustomer
WHERE CustomerID = 101;
GO

--Implement SCD Type 2

UPDATE src.Customers
SET City = 'Pune'
WHERE CustomerID = 101;
GO


TRUNCATE TABLE stg.CustomerStage;

INSERT INTO stg.CustomerStage
(
    CustomerID,
    CustomerName,
    Email,
    City
)
SELECT
    CustomerID,
    CustomerName,
    Email,
    City
FROM src.Customers;
GO


SELECT
    d.CustomerKey,
    d.CustomerID,
    d.City AS PreviousCity,
    s.City AS NewCity,
    d.StartDate,
    d.EndDate
FROM dim.DimCustomer d
JOIN stg.CustomerStage s
    ON d.CustomerID = s.CustomerID
WHERE d.IsCurrent = 1
  AND d.City <> s.City;
GO

SET XACT_ABORT ON;

DECLARE @EffectiveDate DATE = '2025-09-01';

BEGIN TRY
    BEGIN TRANSACTION;

    -- Capture customers whose Type 2 attribute changed.
    SELECT
        d.CustomerID
    INTO #ChangedCustomers
    FROM dim.DimCustomer d
    JOIN stg.CustomerStage s
        ON d.CustomerID = s.CustomerID
    WHERE d.IsCurrent = 1
      AND d.City <> s.City;

    -- Expire existing versions.
    UPDATE d
    SET
        d.EndDate = @EffectiveDate,
        d.IsCurrent = 0
    FROM dim.DimCustomer d
    JOIN #ChangedCustomers c
        ON d.CustomerID = c.CustomerID
    WHERE d.IsCurrent = 1
      AND d.StartDate < @EffectiveDate;

    -- Insert new versions.
    INSERT INTO dim.DimCustomer
    (
        CustomerID,
        CustomerName,
        Email,
        City,
        StartDate,
        EndDate,
        IsCurrent
    )
    SELECT
        s.CustomerID,
        s.CustomerName,
        s.Email,
        s.City,
        @EffectiveDate,
        '9999-12-31',
        1
    FROM stg.CustomerStage s
    JOIN #ChangedCustomers c
        ON s.CustomerID = c.CustomerID;

    DROP TABLE #ChangedCustomers;

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    THROW;
END CATCH;
GO

SELECT
    CustomerKey,
    CustomerID,
    CustomerName,
    City,
    StartDate,
    EndDate,
    IsCurrent
FROM dim.DimCustomer
WHERE CustomerID = 101
ORDER BY StartDate;
GO

INSERT INTO src.Sales
(
    SalesID,
    CustomerID,
    ProductID,
    StoreID,
    SalesDate,
    Quantity,
    UnitPrice
)
VALUES
(
    11,
    101,
    201,
    3,
    '2025-10-10',
    1,
    55000
);
GO

INSERT INTO fact.FactSales
(
    SalesID,
    DateKey,
    CustomerKey,
    ProductKey,
    StoreKey,
    Quantity,
    UnitPrice,
    SalesAmount
)
SELECT
    s.SalesID,
    d.DateKey,
    c.CustomerKey,
    p.ProductKey,
    st.StoreKey,
    s.Quantity,
    s.UnitPrice,
    s.Quantity * s.UnitPrice
FROM src.Sales s
JOIN dim.DimDate d
    ON s.SalesDate = d.FullDate
JOIN dim.DimCustomer c
    ON s.CustomerID = c.CustomerID
   AND s.SalesDate >= c.StartDate
   AND s.SalesDate < c.EndDate
JOIN dim.DimProduct p
    ON s.ProductID = p.ProductID
JOIN dim.DimStore st
    ON s.StoreID = st.StoreID
WHERE NOT EXISTS
(
    SELECT 1
    FROM fact.FactSales f
    WHERE f.SalesID = s.SalesID
);
GO

SELECT
    f.SalesID,
    d.FullDate AS SalesDate,
    c.CustomerName,
    c.City AS HistoricalCustomerCity,
    f.SalesAmount
FROM fact.FactSales f
JOIN dim.DimCustomer c
    ON f.CustomerKey = c.CustomerKey
JOIN dim.DimDate d
    ON f.DateKey = d.DateKey
WHERE c.CustomerID = 101
ORDER BY d.FullDate;
GO

--Analytical SQL Queries on DW
SELECT
    COUNT(*) AS TotalTransactions,
    SUM(Quantity) AS TotalUnitsSold,
    SUM(SalesAmount) AS TotalRevenue,
    AVG(SalesAmount) AS AvgTransactionValue
FROM fact.FactSales;
GO

SELECT
    d.YearNumber,
    d.MonthNumber,
    d.MonthName,
    SUM(f.SalesAmount) AS TotalRevenue
FROM fact.FactSales f
JOIN dim.DimDate d
    ON f.DateKey = d.DateKey
GROUP BY
    d.YearNumber,
    d.MonthNumber,
    d.MonthName
ORDER BY
    d.YearNumber,
    d.MonthNumber;
GO

SELECT
    p.Category,
    COUNT(*) AS TransactionCount,
    SUM(f.Quantity) AS UnitsSold,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimProduct p
    ON f.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY Revenue DESC;
GO


SELECT TOP 5
    p.ProductName,
    p.Category,
    SUM(f.Quantity) AS UnitsSold,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimProduct p
    ON f.ProductKey = p.ProductKey
GROUP BY
    p.ProductName,
    p.Category
ORDER BY Revenue DESC;
GO

SELECT
    st.StoreName,
    st.City,
    st.Region,
    COUNT(*) AS Transactions,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimStore st
    ON f.StoreKey = st.StoreKey
GROUP BY
    st.StoreName,
    st.City,
    st.Region
ORDER BY Revenue DESC;
GO


WITH CustomerRevenue AS
(
    SELECT
        c.CustomerID,
        MAX(c.CustomerName) AS CustomerName,
        SUM(f.SalesAmount) AS Revenue
    FROM fact.FactSales f
    JOIN dim.DimCustomer c
        ON f.CustomerKey = c.CustomerKey
    GROUP BY c.CustomerID
)
SELECT
    CustomerID,
    CustomerName,
    Revenue,
    DENSE_RANK() OVER
    (
        ORDER BY Revenue DESC
    ) AS RevenueRank
FROM CustomerRevenue
ORDER BY RevenueRank, CustomerID;
GO

WITH MonthlySales AS
(
    SELECT
        d.YearNumber,
        d.MonthNumber,
        SUM(f.SalesAmount) AS Revenue
    FROM fact.FactSales f
    JOIN dim.DimDate d
        ON f.DateKey = d.DateKey
    GROUP BY
        d.YearNumber,
        d.MonthNumber
),
PreviousMonth AS
(
    SELECT
        YearNumber,
        MonthNumber,
        Revenue,
        LAG(Revenue) OVER
        (
            ORDER BY YearNumber, MonthNumber
        ) AS PreviousRevenue
    FROM MonthlySales
)
SELECT
    YearNumber,
    MonthNumber,
    Revenue,
    PreviousRevenue,
    ROUND(
        100.0 * (Revenue - PreviousRevenue)
        / NULLIF(PreviousRevenue, 0),
        2
    ) AS GrowthPercentage
FROM PreviousMonth
ORDER BY YearNumber, MonthNumber;
GO


WITH DailySales AS
(
    SELECT
        d.FullDate,
        SUM(f.SalesAmount) AS DailyRevenue
    FROM fact.FactSales f
    JOIN dim.DimDate d
        ON f.DateKey = d.DateKey
    GROUP BY d.FullDate
)
SELECT
    FullDate,
    DailyRevenue,
    SUM(DailyRevenue) OVER
    (
        ORDER BY FullDate
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND CURRENT ROW
    ) AS RunningRevenue
FROM DailySales
ORDER BY FullDate;
GO


SELECT
    c.City AS HistoricalCity,
    COUNT(*) AS Transactions,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimCustomer c
    ON f.CustomerKey = c.CustomerKey
GROUP BY c.City
ORDER BY Revenue DESC;
GO


SELECT
    historical.City AS CityAtSale,
    currentdim.City AS CurrentCity,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimCustomer historical
    ON f.CustomerKey = historical.CustomerKey
JOIN dim.DimCustomer currentdim
    ON historical.CustomerID = currentdim.CustomerID
   AND currentdim.IsCurrent = 1
GROUP BY
    historical.City,
    currentdim.City
ORDER BY Revenue DESC;
GO

--Data Warehouse Validation

SELECT
    (SELECT COUNT(*) FROM src.Sales)
        AS SourceCount,
    (SELECT COUNT(*) FROM fact.FactSales)
        AS FactCount;
GO


SELECT
    (SELECT SUM(Quantity * UnitPrice)
     FROM src.Sales) AS SourceRevenue,

    (SELECT SUM(SalesAmount)
     FROM fact.FactSales) AS WarehouseRevenue;
GO


SELECT
    CustomerID,
    COUNT(*) AS CurrentVersionCount
FROM dim.DimCustomer
WHERE IsCurrent = 1
GROUP BY CustomerID
HAVING COUNT(*) > 1;
GO


WITH Versions AS
(
    SELECT
        CustomerID,
        StartDate,
        EndDate,
        LAG(EndDate) OVER
        (
            PARTITION BY CustomerID
            ORDER BY StartDate
        ) AS PreviousEndDate
    FROM dim.DimCustomer
)
SELECT *
FROM Versions
WHERE PreviousEndDate > StartDate;
GO


SELECT
    f.SalesID,
    d.FullDate,
    c.CustomerID,
    c.StartDate,
    c.EndDate
FROM fact.FactSales f
JOIN dim.DimCustomer c
    ON f.CustomerKey = c.CustomerKey
JOIN dim.DimDate d
    ON f.DateKey = d.DateKey
WHERE NOT
(
    d.FullDate >= c.StartDate
    AND d.FullDate < c.EndDate
);
GO


SELECT
    c.CustomerID,
    MAX(c.CustomerName) AS CustomerName,
    SUM(f.SalesAmount) AS Revenue
FROM fact.FactSales f
JOIN dim.DimCustomer c
    ON f.CustomerKey = c.CustomerKey
GROUP BY c.CustomerID
ORDER BY Revenue DESC;
GO