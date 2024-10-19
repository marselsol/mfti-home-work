import asyncio

async def compute_square(number):
    await asyncio.sleep(1)
    print(f"Квадрат числа {number} равен {number ** 2}")

async def main():
    tasks = [compute_square(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
