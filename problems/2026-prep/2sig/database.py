from typing import List, Optional, Tuple, Any

class Database:
    def __init__(self):
        self.records = []
        # Stores field -> value -> list of record IDs
        # e.g., {'city': {'NYC':}}
        self.inverted_indexes = {}
        self.id_counter = 0

    def insert(self, record: dict):
        self.records.append(record)
        for field, value in record.items():
            if field not in self.inverted_indexes:
                self.inverted_indexes[field] = {}

            if value not in self.inverted_indexes[field]:
                self.inverted_indexes[field][value] = []

            self.inverted_indexes[field][value].append(self.id_counter)
        self.id_counter += 1

class QueryParser:
    def __init__(self):
        self.operators = {
            '=': lambda a, b: a == b,
            '>': lambda a, b: a is not None and a > b,
            '<': lambda a, b: a is not None and a < b,
            '<=': lambda a, b: a is not None and a <= b,
            '>=': lambda a, b: a is not None and a >= b,
            '!=': lambda a, b: a != b
        }

    def _cast_value(self, val_str: str) -> Any:
        """Helper to cast the string value from the query to the correct type."""
        val_str = val_str.strip().strip("'").strip('"') # Remove whitespace and quotes
        try:
            return int(val_str)
        except ValueError:
            try:
                return float(val_str)
            except ValueError:
                return val_str # Leave as string if it's not a number

    def parse(self, query: str) -> Tuple[List[dict], Optional[dict]]:
        conditions, order_by = [], None
        
        # 1. Parse WHERE clause
        if "WHERE" in query:
            where_part = query.split("WHERE").split("ORDER BY").strip()
            for condition in where_part.split("AND"):
                condition = condition.strip()
                
                # BUG FIX: Order matters! If we check ">" before ">=", a string 
                # like "age >= 30" will match ">" and leave "= 30" as the value.
                # We must check 2-character operators first.
                for operation in ["!=", "<=", ">=", "=", "<", ">"]:
                    if operation in condition:
                        field, value_str = condition.split(operation)
                        conditions.append({
                            'field': field.strip(),
                            'value': self._cast_value(value_str), # ADDRESSES TODO: Type casting
                            'operator': operation
                        })
                        break

        # 2. Parse ORDER BY clause
        if "ORDER BY" in query:
            order_part = query.split("ORDER BY").strip()
            parts = order_part.split()
            field = parts
            # Check for DESC or ASC direction
            reverse = True if len(parts) > 1 and parts.upper() == 'DESC' else False
            order_by = {'field': field, 'reverse': reverse} # ADDRESSES TODO: Order By values

        return conditions, order_by
    
    def evaluate(self, record: dict, conditions: List[dict]) -> bool:
        return all(self.operators[c['operator']](record.get(c['field']), c['value']) for c in conditions)

class QueryExecutor:
    def __init__(self, database: Database, parser: QueryParser):
        self.db = database
        self.parser = parser

    def execute(self, query: str) -> List[dict]:
        conditions, order_by = self.parser.parse(query)
        candidate_ids = self.get_candidate_records(conditions)
        
        results = []
        for rid in candidate_ids:
            if self.parser.evaluate(self.db.records[rid], conditions):
                results.append(self.db.records[rid])

        # Apply sorting if ORDER BY was parsed
        if order_by:
            field = order_by['field']
            reverse = order_by['reverse']
            # Fallback to 0 or empty string if field is missing to prevent crash
            results.sort(key=lambda r: r.get(field, 0 if isinstance(r.get(field), int) else ""), reverse=reverse)
            
        return results

    def get_candidate_records(self, conditions: List[dict]) -> set:
        """
        ADDRESSES TODO: We should look at ALL equality conditions to narrow down our 
        candidates as much as possible before evaluating!
        """
        eq_conditions = [c for c in conditions if c['operator'] == '=']
        
        if not eq_conditions:
            # No indexable conditions, return all IDs
            return set(range(self.db.id_counter))
        
        # Intersect all '=' conditions. 
        # If city='NYC' AND age=30, we find the IDs for both and find the overlapping ones.
        candidate_sets = []
        for eq in eq_conditions:
            field, value = eq['field'], eq['value']
            # Find the IDs for this specific field=value match
            ids_for_condition = self.db.inverted_indexes.get(field, {}).get(value, [])
            candidate_sets.append(set(ids_for_condition))
            
        # The ultimate optimization: Intersect the sets to find only records that match ALL '=' conditions
        final_candidates = set.intersection(*candidate_sets)
        return final_candidates

class InMemoryDatabase:
    def __init__(self):
        self.storage = Database()
        self.parser = QueryParser()
        self.executor = QueryExecutor(self.storage, self.parser)

    def insert(self, record: dict):
        self.storage.insert(record)

    def query(self, sql_string: str) -> List[dict]:
        return self.executor.execute(sql_string)

# ==========================================
# USAGE EXAMPLE & TESTING
# ==========================================
if __name__ == "__main__":
    db = InMemoryDatabase()
    db.insert({'id': 1, 'name': 'Alice', 'age': 30, 'city': 'NYC'})
    db.insert({'id': 2, 'name': 'Bob', 'age': 25, 'city': 'LA'})
    db.insert({'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'NYC'})
    db.insert({'id': 4, 'name': 'David', 'age': 30, 'city': 'NYC'})
    
    print("Executing: SELECT * WHERE city = 'NYC' AND age >= 30 ORDER BY age DESC")
    results = db.query("SELECT * WHERE city = 'NYC' AND age >= 30 ORDER BY age DESC")
    
    for r in results:
        print(r)