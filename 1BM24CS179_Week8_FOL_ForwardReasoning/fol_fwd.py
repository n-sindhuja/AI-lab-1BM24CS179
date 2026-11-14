
# FOL Forward Chaining Algorithm

# Initial Knowledge Base (Facts)
KB = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

# Forward Chaining Algorithm
def forward_chaining(KB, query):

    while True:
        new = set()

        # Rule 1: Missile(x) -> Weapon(x)
        for fact in KB:
            if fact[0] == "Missile":
                x = fact[1]
                inferred = ("Weapon", x)

                if inferred not in KB:
                    new.add(inferred)

        # Rule 2: Missile(x) AND Owns(A,x)
        #         -> Sells(Robert,x,A)
        for missile in KB:
            if missile[0] == "Missile":
                x = missile[1]

                if ("Owns", "A", x) in KB:
                    inferred = ("Sells", "Robert", x, "A")

                    if inferred not in KB:
                        new.add(inferred)

        # Rule 3: Enemy(x,America) -> Hostile(x)
        for fact in KB:
            if fact[0] == "Enemy" and fact[2] == "America":
                x = fact[1]
                inferred = ("Hostile", x)

                if inferred not in KB:
                    new.add(inferred)

        # Rule 4: Criminal rule
        for fact in KB:
            if fact[0] == "American":
                x = fact[1]

                for weapon in KB:
                    if weapon[0] == "Weapon":

                        y = weapon[1]

                        for sells in KB:
                            if (sells[0] == "Sells"
                                and sells[1] == x
                                and sells[2] == y):

                                z = sells[3]

                                if ("Hostile", z) in KB:
                                    inferred = ("Criminal", x)

                                    if inferred not in KB:
                                        new.add(inferred)

        # Check whether query is proved
        if query in KB or query in new:
            return True

        # Stop if no new facts are generated
        if not new:
            return False

        # Add newly inferred facts
        print("New facts inferred:", new)
        KB.update(new)


# Given Query
query = ("Criminal", "Robert")

# Execute Forward Chaining
print("Initial Knowledge Base:")
for fact in KB:
    print(fact)

result = forward_chaining(KB, query)

if result:
    print("\nQuery Proved Successfully!")
    print("Criminal(Robert) = True")
else:
    print("\nQuery Cannot Be Proved.")
