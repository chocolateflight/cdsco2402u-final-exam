# Imports
import csv
from datetime import datetime

# ------------------------ Data Classes ------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Person"


class Suspect(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Suspect"


class Victim(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Victim"


class Case:
    def __init__(self, case_id, date, suspect, victim, crime_type, severity, status):
        self.case_id = case_id
        self.date = date
        self.suspect = suspect
        self.victim = victim
        self.crime_type = crime_type
        self.severity = severity
        self.status = status

    def __str__(self):
        date_str = self.date.strftime("%Y-%m-%d")
        return (
            f"Case ID: {self.case_id}, Date: {date_str}, "
            f"Suspect: {self.suspect.name}, Victim: {self.victim.name}, "
            f"Crime Type: {self.crime_type}, Severity: {self.severity}, "
            f"Status: {self.status}"
        )


# ------------------------ Algorithm Classes ------------------------

class SortingAlgorithm:
    def case_attribute(case, attribute):
        if attribute == "case_id":
            return case.case_id

        elif attribute == "date":
            return case.date

        elif attribute == "severity":
            return case.severity

        elif attribute == "status":
            return case.status.lower()

        else:
            return case.case_id  # default

    def merge_sort(self, case_list, sort_attribute):
        if len(case_list) <= 1:
            return case_list

        middle = len(case_list) // 2
        left_half = self.merge_sort(case_list[:middle], sort_attribute)
        right_half = self.merge_sort(case_list[middle:], sort_attribute)

        sorted_cases = []
        left_index = 0
        right_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            left_value = SortingAlgorithm.case_attribute(
                left_half[left_index], sort_attribute
            )
            right_value = SortingAlgorithm.case_attribute(
                right_half[right_index], sort_attribute
            )

            if left_value <= right_value:
                sorted_cases.append(left_half[left_index])
                left_index += 1

            else:
                sorted_cases.append(right_half[right_index])
                right_index += 1

        while left_index < len(left_half):
            sorted_cases.append(left_half[left_index])
            left_index += 1

        while right_index < len(right_half):
            sorted_cases.append(right_half[right_index])
            right_index += 1

        return sorted_cases


class SearchAlgorithm:
    def binary_search(case_list, search_attribute="case_id", search_value=None):
        first = 0
        last = len(case_list) - 1

        try:
            search_value = int(search_value)
        except:
            pass

        while first <= last:
            middle = (first + last) // 2
            middle_value = case_list[middle]

            if search_attribute == "case_id":
                if middle_value.case_id == search_value:
                    return middle_value
                elif middle_value.case_id < search_value:
                    first = middle + 1
                else:
                    last = middle - 1

            else:
                return None

    def linear_search(case_list, search_attribute, search_value):
        results = []

        for case in case_list:
            if search_attribute == "suspect":
                if case.suspect.name.upper() == search_value.upper():
                    results.append(case)

            elif search_attribute == "victim":
                if case.victim.name.upper() == search_value.upper():
                    results.append(case)

        return results


# ------------------------ Case Archive Classes ------------------------

class CaseArchive:
    def __init__(self):
        self.case_list = []

    def load_cases(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8-sig") as f:
                file_data = csv.DictReader(f)
                for case in file_data:
                    case_id_string = case["CaseID"]
                    date_string = case["Date"]
                    suspect_name = case["MainSuspect"]
                    victim_name = case["Victim"]
                    crime_type = case["CrimeType"]
                    severity = case["CaseSeverity"]
                    status = case["Status"]

                    if (
                        not case_id_string
                        or not date_string
                        or not crime_type
                        or not severity
                        or not status
                        or not suspect_name
                        or not victim_name
                        
                    ):
                        raise ValueError(
                            "CSV is missing required fields. Please check that all fields are present."
                        )

                    try:
                        date = datetime.strptime(date_string, "%d/%m/%Y")
                    except ValueError:
                        raise ValueError("Date must be in the format DD/MM/YYYY.")

                    try:
                        case_id = int(case_id_string)
                    except ValueError:
                        raise ValueError("Case ID must be an integer.")

                    try:
                        severity = int(severity)
                    except ValueError:
                        raise ValueError("Severity must be an integer.")

                    suspect = Suspect(suspect_name)
                    victim = Victim(victim_name)

                    new_case = Case(
                        case_id, date, suspect, victim, crime_type, severity, status
                    )
                    self.case_list.append(new_case)

            return True

        except FileNotFoundError:
            raise FileNotFoundError(f"No CSV file found at filepath: {filepath}")

        except Exception as e:
            raise ValueError(f"Error loading cases: {str(e)}")

    def load_demo_cases(self):
        demo_data = [
            {
                "CaseID": "84435",
                "Date": "01/01/1983",
                "CrimeType": "Arson",
                "MainSuspect": "Jeffery Castillo",
                "Victim": "Jennifer Long",
                "CaseSeverity": "7",
                "Status": "Unsolved",
            },
            {
                "CaseID": "86458",
                "Date": "02/02/1983",
                "CrimeType": "Theft",
                "MainSuspect": "Angela Ross",
                "Victim": "James Wilkerson",
                "CaseSeverity": "3",
                "Status": "Solved",
            },
            {
                "CaseID": "62068",
                "Date": "03/03/1983",
                "CrimeType": "Murder",
                "MainSuspect": "Unknown",
                "Victim": "Unknown",
                "CaseSeverity": "10",
                "Status": "Unsolved",
            },
            {
                "CaseID": "49692",
                "Date": "04/04/1983",
                "CrimeType": "Theft",
                "MainSuspect": "Jeremy Green",
                "Victim": "Heidi Mckinney",
                "CaseSeverity": "2",
                "Status": "Solved",
            },
            {
                "CaseID": "24397",
                "Date": "05/05/1983",
                "CrimeType": "Arson",
                "MainSuspect": "Travis Rollins",
                "Victim": "Christina Bartlett",
                "CaseSeverity": "8",
                "Status": "Unsolved",
            },
        ]

        for case in demo_data:
            case_id = int(case["CaseID"])
            date = datetime.strptime(case["Date"], "%m/%d/%Y")
            suspect = Suspect(case["MainSuspect"])
            victim = Victim(case["Victim"])
            crime_type = case["CrimeType"]
            severity = int(case["CaseSeverity"])
            status = case["Status"]
            new_case = Case(
                case_id, date, suspect, victim, crime_type, severity, status
            )
            self.case_list.append(new_case)

    def load_crime_types(self):
        if not self.case_list:
            return []
        crime_types = []
        for case in self.case_list:
            crime_types.append(case.crime_type)
        return list(set(crime_types))

    def no_cases(self):
        if len(self.case_list) == 0:
            print("No cases found. Please load cases first.")
            return True

    def search_suspect(self, suspect_name):
        if self.no_cases():
            return []

        results = SearchAlgorithm.linear_search(self.case_list, "suspect", suspect_name)
        if not results:
            return []
        else:
            return results

    def search_victim(self, victim_name):
        if self.no_cases():
            return []

        results = SearchAlgorithm.linear_search(self.case_list, "victim", victim_name)
        if not results:
            return []
        else:
            return results

    def search_case_id(self, case_id):
        if self.no_cases():
            return []
        
        self.case_list = SortingAlgorithm().merge_sort(self.case_list, "case_id")
        results = SearchAlgorithm.binary_search(self.case_list, "case_id", case_id)
        if not results:
            return []
        else:
            return [results]

    def filter_cases(self, crime_type, severity, status):
        if self.no_cases():
            return []

        results = []
        for case in self.case_list:
            if crime_type is not None and case.crime_type != crime_type:
                continue

            if severity is not None and case.severity != severity:
                continue

            if status is not None and case.status != status:
                continue

            results.append(case)

        if not results:
            return []
        else:
            return results

    def sort_cases(self, sort_attribute):
        if self.no_cases():
            return []

        results = SortingAlgorithm().merge_sort(self.case_list, sort_attribute)

        if not results:
            return []
        else:
            return results


# ------------------------ Application ------------------------

class Application():
    def __init__(self):
        self.case_archive = CaseArchive()
        
    def print_case_results(self, cases):
        if not cases:
            print("\nNo results found.\n")

        else:
            print("\n--- Cases Found ---")
            for case in cases:
                print(case.__str__())
            print("----------\n")

    def menu(self):
        run = True
        while True:
            while run == True:
                print("\n=== MDA Case Archive Management System ===")
                print("1. Search by Suspect Name")
                print("2. Search by Victim Name")
                print("3. Search for Case ID")
                print("4. Filter Cases")
                print("5. Sort Cases")
                print("6. Exit")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    print("\n=== Search by Suspect Name ===")
                    print(
                        """
                    Note: This print message wouldn't be here in a real application.
                    The full list of suspect names is available in the case_archive. 
                    The following names will work in both the demo and loaded cases:
                    Jeffery Castillo, Angela Ross, Unknown, Jeremy Green, Travis Rollins      
                    """
                    )
                    print("Enter suspect name: ")
                    suspect_name = input("Enter suspect name: ").strip().upper()
                    results = self.case_archive.search_suspect(suspect_name)
                    print(f"\n=== Results for suspect: {suspect_name} ===")
                    self.print_case_results(results)
                    continue

                elif choice == "2":
                    print("\n=== Search by Victim Name ===")
                    print(
                        """
                        Note: This print message wouldn't be here in a real application.
                        The full list of victim names is available in the case_archive.
                        The following names will work in both the demo and loaded cases:
                        Jennifer Long, James Wilkerson, Unknown, Heidi Mckinney, Christina Bartlett
                        """
                    )
                    print("Enter victim name: ")
                    victim_name = input("Enter victim name: ").strip().upper()
                    results = self.case_archive.search_victim(victim_name)
                    print(f"\n=== Results for victim: {victim_name} ===")
                    self.print_case_results(results)
                    continue

                elif choice == "3":
                    print("\n=== Search for Case ID ===")
                    print(
                        """
                        Note: This print message wouldn't be here in a real application.
                        The full list of case IDs is available in the case_archive.
                        The following case IDs will work in both the demo and loaded cases:
                        84435, 86458, 62068, 49692, 24397
                        """
                    )
                    print("Enter case ID: ")
                    try:
                        case_id = int(input("Enter case ID: ").strip())
                    except ValueError:
                        print("Case ID must be an integer.")
                        continue
                    results = self.case_archive.search_case_id(case_id)
                    self.print_case_results(results)
                    continue

                elif choice == "4":
                    while True:
                        print("\n=== Filter Cases ===")
                        print("1. Filter by Crime Type")
                        print("2. Filter by Severity")
                        print("3. Filter by Status")
                        print("4. Back")

                        filter_choice = input("Enter your choice: ").strip()

                        if filter_choice == "1":
                            while True:
                                print("\n=== Filter by Crime Type ===")
                                print("Select a crime type:")

                                crime_types = self.case_archive.load_crime_types()
                                for i, crime_type in enumerate(crime_types):
                                    print(f"{i + 1}. {crime_type}")

                                crime_type = input("Enter crime type: ").strip()

                                try:
                                    crime_type = int(crime_type)

                                except ValueError:
                                    print("Invalid choice. Please try again.")
                                    continue

                                if crime_type < 1 or crime_type > len(crime_types):
                                    print("Invalid choice. Please try again.")
                                    continue

                                crime_type = crime_types[crime_type - 1]
                                break

                            results = self.case_archive.filter_cases(crime_type, None, None)
                            print(f"\n=== Results for crime type: {crime_type} ===")
                            self.print_case_results(results)
                            break

                        elif filter_choice == "2":
                            print("=== Filter by Severity ===")
                            print("Enter a severity level (1-10):")
                            try:
                                severity = int(input("Enter severity: ").strip())
                            except ValueError:
                                print("Severity must be an integer.")
                                continue
                            results = self.case_archive.filter_cases(None, severity, None)
                            print(f"\n=== Results for severity: {severity} ===")
                            self.print_case_results(results)
                            break

                        elif filter_choice == "3":
                            while True:
                                print("\n=== Filter by Status ===")
                                print("Status options: Unsolved, Solved")
                                print("1. Unsolved")
                                print("2. Solved")
                                status_choice = input(
                                    "Select Status to filter (1 Unsolved, 2 Solved): "
                                ).strip()

                                if status_choice == "1":
                                    status = "Unsolved"
                                elif status_choice == "2":
                                    status = "Solved"
                                else:
                                    print("Invalid choice. Please try again.")
                                    continue

                                results = self.case_archive.filter_cases(None, None, status)
                                print(f"\n=== Results for status: {status} ===")
                                self.print_case_results(results)
                                break

                        elif filter_choice == "4":
                            break

                        else:
                            print("Invalid choice. Please try again.")
                            continue

                elif choice == "5":
                    while True:
                        print("\n=== Sort Cases ===")
                        print("1. Sort by Case ID")
                        print("2. Sort by Date")
                        print("3. Sort by Severity")
                        print("4. Sort by Status")
                        print("5. Back")

                        sort_choice = input("Enter your choice: ").strip()

                        if sort_choice == "1":
                            results = self.case_archive.sort_cases("case_id")
                            print(f"\n=== Results sorted by case ID ===")
                            self.print_case_results(results)
                            break

                        elif sort_choice == "2":
                            results = self.case_archive.sort_cases("date")
                            print(f"\n=== Results sorted by date ===")
                            self.print_case_results(results)
                            break

                        elif sort_choice == "3":
                            results = self.case_archive.sort_cases("severity")
                            print(f"\n=== Results sorted by severity ===")
                            self.print_case_results(results)
                            break

                        elif sort_choice == "4":
                            results = self.case_archive.sort_cases("status")
                            print(f"\n=== Results sorted by status ===")
                            self.print_case_results(results)
                            break

                        elif sort_choice == "5":
                            break

                        else:
                            print("Invalid choice. Please try again.")
                            continue

                elif choice == "6":
                    run = False
                    break

                else:
                    print("Invalid choice. Please try again.")
                    continue

            print(
                "\nThank you for using the MDA Case Archive Management System. Goodbye - and happy case solving!"
            )
            break
     
    def run(self):
        while True:
            print(
                """
            +-+-+-+ +-+ +-+-+-+-+ +-+-+-+-+-+-+-+
            |M|D|A| |-| |C|a|s|e| |A|r|c|h|i|v|e|
            +-+-+-+ +-+ +-+-+-+-+ +-+-+-+-+-+-+-+
        """
            )
            print("=== Welcome to the Metropolitan Detective Agency Case Archive ===")
            print("Select an option:")
            print("1. Load Cases")
            print("2. Exit")
            user_choice = input("Enter choice: ").strip()

            if user_choice == "1":
                print("Loading cases from case_archive at filepath: case_archive.csv")

                try:
                    self.case_archive.load_cases("case_archive.csv")
                    print("Cases loaded successfully.")
                    self.menu()
                    break

                except Exception as e:
                    print(f"Failed to load cases: {str(e)}")
                    print("Select an option to proceed:")
                    print("1. Load Demo Cases")
                    print("2. Exit")

                    sub_user_choice = input("Enter choice: ").strip()

                    if sub_user_choice == "1":
                        self.case_archive.load_demo_cases()
                        print("Demo cases loaded successfully.")
                        self.menu()
                        break

                    elif sub_user_choice == "2":
                        print("Exiting program.")
                        break

                    else:
                        print("Invalid choice. Returning to main menu.")
                        continue

            elif user_choice == "2":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")
                continue


# ------------------------ Run Program ------------------------

app = Application()
app.run()