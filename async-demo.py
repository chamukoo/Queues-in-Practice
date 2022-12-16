from mod.async_queues import Job

job1 = Job("http://localhost/")
job2 = Job("https://localhost:8080/")

print("\n\n\n" + ("="*60) + "\n\n\t\tasyncio.PriorityQueue\n\n" + ("="*60))
print("\n\n\t⭐ ASYNC DEMO\n" + ("-"*60) + "\n")
print("\t", job1 < job2)
print("\n" + ("="*60) + "\n\n\n")

