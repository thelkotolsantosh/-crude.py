import argparse
import sqlite3


def main():
    parser = argparse.ArgumentParser(description="Keep a local register of purchase requests.")
    parser.add_argument("--db", default="requests.sqlite")
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("add").add_argument("item")
    commands.add_parser("list")
    edit = commands.add_parser("edit")
    edit.add_argument("id", type=int)
    edit.add_argument("item")
    commands.add_parser("delete").add_argument("id", type=int)
    args = parser.parse_args()
    if hasattr(args, "item") and not args.item.strip():
        parser.error("Enter an item name.")
    with sqlite3.connect(args.db) as db:
        db.execute("CREATE TABLE IF NOT EXISTS requests(id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL)")
        if args.action == "add":
            print(db.execute("INSERT INTO requests(item) VALUES (?)", (args.item.strip(),)).lastrowid)
        elif args.action == "list":
            for number, item in db.execute("SELECT id,item FROM requests ORDER BY id"):
                print(number, item)
        else:
            if args.action == "edit":
                result = db.execute("UPDATE requests SET item=? WHERE id=?", (args.item.strip(), args.id))
            else:
                result = db.execute("DELETE FROM requests WHERE id=?", (args.id,))
            if not result.rowcount:
                parser.error("No request has that ID.")


if __name__ == "__main__":
    main()
