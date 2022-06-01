from subprocess import Popen, PIPE

from app.database import Database

if __name__ == "__main__":
    # db = Database("./db.json")
    # db.open()
    # st = db.to_str()
    # print(st)

    with Popen(["stack", "ghci"], stdout=PIPE) as proc:
        print(proc.stdout.read())
        print("1")
        proc.stdin.write(b":l ./course.hs")
        print("2")
        print(proc.stdout.read())