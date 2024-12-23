from asyncio import run

from core.scripts.leave_comments import leave_comments


async def main():
    await leave_comments()


if __name__ == '__main__':
    run(main())
