## Exercise 1.1

**(a)** Let $R$ be the relation scheme `{ EMPLOYEE, MANAGER, JOB, SALARY,
YEARS-WORKED }`, where `EMPLOYEE` and `MANAGER` are names. `JOB` is a title.
`SALARY` is yearly salary, and `YEARS-WORKED` is the number of complete years
the employee has been at the job. Construct a relation on $R$ based on the
following information.

1. Roberts, Ruskin, and Raphael are all ticket agents.
2. Rayburn is a baggage handler.
3. Rice is a flight mechanic.
4. Price manages all ticket agents.
5. Powell manages Rayburn.
6. Porter manages Rice, Price, Powell and himself.
7. Powell is head of ground crews and Porter is chief of operations.
8. Every employee receives a 10% raise for each complete year worked.
9. Roberts, Ruskin, Raphael, and Rayburn all started at $12,000. Roberts just
   started work, Ruskin and Raphael have worked for a year and a half, and
   Rayburn has worked for 2 years.
10. Rice started at $18,000 and now makes $21,780.
11. Price and Powell started at $16,000 and have both been working for three
	years.
12. Porter started at $20,000 and has been around two years longer than anyone
	else.

| Employee | Manager | Job                  | Salary     | Years Worked |
| ---      | ---     | ---                  | ---        | ---          |
| Roberts  | Price   | Ticket Agent         | $12,000.00 | 0            |
| Ruskin   | Price   | Ticket Agent         | $13,200.00 | 1.5          |
| Raphael  | Price   | Ticket Agent         | $13,200.00 | 1.5          |
| Rayburn  | Powell  | Mechanical Engineer  | $14,520.00 | 2            |
| Rice     | Porter  | Flight Mechanic      | $21,780.00 | 2            |
| Powell   | Porter  | Head of Ground Crews | $21,296.00 | 3            |
| Price    | Porter  | Ticket Agent Manager | $21,296.00 | 3            |
| Porter   | Porter  | Chief of Operations  | $32,210.20 | 5            |

> This was fun. It reminds me a lot of those Einstein's Logic Puzzles.

**(b)** Give appropriate update operations for the following changes to the
relation for part (a):

1. Ruskin and Raphael complete their second year.

```
CHANGE (R; Employee=Ruskin; Salary=$14,520.00, Years-Worked=2)
CHANGE (R; Employee=Raphael; Salary=$14,520.00, Years-Worked=2)
```

2. Rice quits.

```
DELETE (R; Employee=Rice)
```

3. Powell quits. His duties are assumed by Porter.

```
DELETE (R; Employee=Powell)
CHANGE (R; Employee=Porter; Job=Chief of Operations/Head of Ground Crews)

The CHANGE operation makes the relation break first normal form (1NF) because
now the domain of the JOB attribute does not contain atomic values.
```

4. Randolph is hired as a ticket agent.

```
ADD (R; Employee=Randolph, Manager=Price, Job=Ticket Agent, Salary=$12,000.00, Years-Worked=0)
```
