from employee_utils.salary import (
    calculate_gross_salary,
    calculate_net_salary
)

from employee_utils.reports import print_salary_report

def main():
    name = "Rahul"

    gross = calculate_gross_salary(
        50000, 10000, 5000
    )

    tax = gross * 0.10
    net = calculate_net_salary(gross, tax)

    print_salary_report(name, gross, net)


if __name__ == "__main__":
    main()