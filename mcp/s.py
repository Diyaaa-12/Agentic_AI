from mcp.server.mcpserver import MCPServer

mcp = MCPServer("College Server")


students = {
    "ravi": {
        "name": "Ravi",
        "marks": {
            "python": 85,
            "ai": 90,
            "dbms": 78
        },
        "attendance": 87
    },
    "praveen": {
        "name": "Praveen",
        "marks": {
            "python": 92,
            "ai": 88,
            "dbms": 95
        },
        "attendance": 91
    }
}


@mcp.tool()
def get_student(name: str) -> dict:
    """Get complete information about a student."""
    return students.get(
        name.lower(),
        {"error": "Student not found"}
    )


@mcp.tool()
def get_marks(name: str) -> dict:
    """Get marks of a student."""
    student = students.get(name.lower())

    if not student:
        return {"error": "Student not found"}

    return student["marks"]


@mcp.tool()
def get_attendance(name: str) -> str:
    """Get attendance percentage of a student."""
    student = students.get(name.lower())

    if not student:
        return "Student not found"

    return f"{student['name']} attendance is {student['attendance']}%"


@mcp.tool()
def calculate_average(name: str) -> float:
    """Calculate average marks of a student."""
    student = students.get(name.lower())

    if not student:
        return 0.0

    marks = student["marks"].values()

    return sum(marks) / len(marks)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000
    )