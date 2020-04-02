class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        dfs = lambda id: sum([dfs(sub_id) for sub_id in emps[id].subordinates]) + emps[id].importance
        return dfs(id)         