#!/usr/bin/env python3
"""
Vacation Coverage Analysis - Basic Data Demo Script

This script demonstrates fundamental data operations for vacation coverage analysis.
It performs simple calculations and data manipulation without external datasets.

Author: Data Analysis Team
Date: March 2026
"""

def main():
    """
    Main function to execute the vacation data analysis demonstration.
    """
    
    print("="*60)
    print("VACATION COVERAGE ANALYSIS - DATA DEMO")
    print("="*60)
    print()
    
    # Part 1: Employee Vacation Data Setup
    print("1. Setting up sample employee vacation data...")
    
    # Sample employee data with vacation days
    employees = {
        "Alice Johnson": {"department": "Engineering", "vacation_days": 15, "used_days": 8},
        "Bob Smith": {"department": "Marketing", "vacation_days": 20, "used_days": 12},
        "Carol Davis": {"department": "Engineering", "vacation_days": 15, "used_days": 5},
        "David Wilson": {"department": "HR", "vacation_days": 18, "used_days": 15},
        "Emma Brown": {"department": "Marketing", "vacation_days": 20, "used_days": 20}
    }
    
    print(f"Total employees in dataset: {len(employees)}")
    print()
    
    # Part 2: Basic Calculations
    print("2. Performing basic vacation usage calculations...")
    
    total_allocated_days = 0
    total_used_days = 0
    remaining_days_by_employee = {}
    
    for name, data in employees.items():
        allocated = data["vacation_days"]
        used = data["used_days"]
        remaining = allocated - used
        
        total_allocated_days += allocated
        total_used_days += used
        remaining_days_by_employee[name] = remaining
        
        print(f"  {name}: {used}/{allocated} days used, {remaining} remaining")
    
    print()
    
    # Part 3: Summary Statistics
    print("3. Calculating summary statistics...")
    
    usage_percentage = (total_used_days / total_allocated_days) * 100
    average_allocation = total_allocated_days / len(employees)
    average_usage = total_used_days / len(employees)
    
    print(f"  Total vacation days allocated: {total_allocated_days}")
    print(f"  Total vacation days used: {total_used_days}")
    print(f"  Overall usage percentage: {usage_percentage:.1f}%")
    print(f"  Average allocation per employee: {average_allocation:.1f} days")
    print(f"  Average usage per employee: {average_usage:.1f} days")
    print()
    
    # Part 4: Department Analysis
    print("4. Analyzing vacation usage by department...")
    
    dept_stats = {}
    
    for name, data in employees.items():
        dept = data["department"]
        if dept not in dept_stats:
            dept_stats[dept] = {"allocated": 0, "used": 0, "employees": 0}
        
        dept_stats[dept]["allocated"] += data["vacation_days"]
        dept_stats[dept]["used"] += data["used_days"]
        dept_stats[dept]["employees"] += 1
    
    for dept, stats in dept_stats.items():
        dept_usage_pct = (stats["used"] / stats["allocated"]) * 100
        print(f"  {dept}: {stats['used']}/{stats['allocated']} days " +
              f"({dept_usage_pct:.1f}% usage) - {stats['employees']} employees")
    
    print()
    
    # Part 5: Identifying Coverage Risk
    print("5. Identifying potential coverage risks...")
    
    high_usage_employees = []
    low_remaining_employees = []
    
    for name, remaining in remaining_days_by_employee.items():
        usage_rate = (employees[name]["used_days"] / employees[name]["vacation_days"]) * 100
        
        if usage_rate > 80:
            high_usage_employees.append(name)
        
        if remaining <= 3:
            low_remaining_employees.append(name)
    
    print(f"  Employees with >80% usage: {len(high_usage_employees)}")
    for emp in high_usage_employees:
        print(f"    - {emp}")
    
    print(f"  Employees with ≤3 days remaining: {len(low_remaining_employees)}")
    for emp in low_remaining_employees:
        print(f"    - {emp}")
    
    print()
    
    # Part 6: Final Summary
    print("6. Executive Summary")
    print("-" * 30)
    
    total_remaining = sum(remaining_days_by_employee.values())
    
    print(f"• Company-wide vacation usage: {usage_percentage:.1f}%")
    print(f"• Total unused vacation days: {total_remaining}")
    print(f"• Departments tracked: {len(dept_stats)}")
    print(f"• Employees requiring coverage planning: {len(low_remaining_employees)}")
    
    if usage_percentage < 60:
        print("• Status: LOW usage - Encourage vacation time")
    elif usage_percentage < 80:
        print("• Status: MODERATE usage - Monitor coverage")
    else:
        print("• Status: HIGH usage - Plan coverage carefully")
    
    print()
    print("="*60)
    print("Analysis complete! Script executed successfully.")
    print("="*60)


if __name__ == "__main__":
    """
    Script entry point - runs the main analysis function.
    This ensures the script only runs when executed directly, not when imported.
    """
    main()