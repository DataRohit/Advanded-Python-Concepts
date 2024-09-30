import asyncio


# Define an asynchronous coroutine
async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Data fetched successfully!")
    return {"data": [1, 2, 3, 4, 5]}

# Define another asynchronous coroutine that depends on fetch_data
async def process_data():
    print("Processing data...")
    data = await fetch_data()
    print(f"Processed data: {data["data"]}")

# Run the async functions
async def main():
    print("Main coroutine started")
    await process_data()  # Run the process_data coroutine
    print("Main coroutine finished")


# Entry point to run the async code
if __name__ == "__main__":
    asyncio.run(main())