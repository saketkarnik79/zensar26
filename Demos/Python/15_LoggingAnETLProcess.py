# Logging an ETL Process

import logging

logging.basicConfig(
    filename="etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def process_sales(sales):
    logging.info("Sales processing started")

    try:
        if not sales:
            raise ValueError("Sales list is empty")

        total = sum(sales)
        average = total / len(sales)

        logging.info("Sales processed successfully")

        return total, average

    except (ValueError, TypeError) as error:
        logging.error("Processing failed: %s", error)
        raise

    finally:
        logging.info("Sales processing finished")


try:
    total, average = process_sales(
        [1000, 2000, 3000]
    )

    print("Total:", total)
    print("Average:", average)

except (ValueError, TypeError) as error:
    print("Unable to process sales:", error)