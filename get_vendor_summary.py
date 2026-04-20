import sqlite3
import pandas as pd 
import logging
from ingestion.db import ingest_db

logging.basicConfig(
    filename = "logs/get_vendor_summary.log"
    level = logging.DEBUG
    format = "%(asctime)%-%(levelname)s-%(message)s", 
    filemode = "a"
)

def create_vendor_summary(conn):
    """
    This function merges different tables to get overall vendor summary
    and adds new calculated columns.
    """

    query = """
    WITH FreightSummary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY 
            p.VendorNumber, p.VendorName, p.Brand, 
            p.Description, p.PurchasePrice, 
            pp.Price, pp.Volume
    ),

    SalesSummary AS (
        SELECT 
            VendorNo AS VendorNumber,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT 
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost,

        -- Calculations
        (ss.TotalSalesDollars - ps.TotalPurchaseDollars) AS GrossProfit,

        CASE 
            WHEN ss.TotalSalesDollars = 0 THEN 0
            ELSE (ss.TotalSalesDollars - ps.TotalPurchaseDollars) / ss.TotalSalesDollars
        END AS ProfitMargin,

        CASE 
            WHEN ps.TotalPurchaseQuantity = 0 THEN 0
            ELSE ss.TotalSalesQuantity / ps.TotalPurchaseQuantity
        END AS StockTurnover,

        CASE 
            WHEN ps.TotalPurchaseDollars = 0 THEN 0
            ELSE ss.TotalSalesDollars / ps.TotalPurchaseDollars
        END AS SalesToPurchaseRatio

    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNumber
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber

    ORDER BY ps.TotalPurchaseDollars DESC
    """

    vendor_sales_summary = pd.read_sql_query(query, conn)

    return vendor_sales_summary 
