config = {
    # Main title of the page
    "title": "Demo",

    # Refresh the status page (in seconds)
    "refresh": 60,

    # Output directory
    "outputpath": "./docs/",

    # Log directory
    "logpath": "./logs/",

    # Output name
    "outputname": "index.html",

    # How many previous results should be kept
    "history": 91,

    # Short description at the top of the page
    "desc": """<strong>Simple Digital Heartbeat</strong> is a lightweight pure HTML/CSS status page. You can easily add sections. Each tests will execute a simple bash command. If the result is 0 the test is considered as a success. If anything else is returned it is considered as a failure.<br /><br />The full documentation can be found on the <a
      href="https://github.com/Urban-Hacker/DigitalHeartbeat">github</a> page.""",

    # What to display when one or more services are failing
    "popup": "This message will be automatically displayed in case of one or more failure(s).<br /><br />It can be customized by using <strong>basic HTML</strong> like any other text field.",

    # Sections that contains tests
    "sections": [
        {
            # Title of a section
            "title": "London Datacenter",

            # Type of sections (two are allowed: tests and text)
            "type": "tests",

            # Tests that will be performed in the section
            "tests": [
                {"name": "Main Server",
                    "cmd": "echo 1"},
                {"name": "Router",
                 "cmd": "echo 1"},
                {"name": "Mail Server ELIAD",
                 "cmd": "echo 1"},
                {"name": "Mail Server DAVID",
                 "cmd": "echo 1"}
            ]
        },
        {
            "title": "Internal Network",
            "type": "tests",
            "tests": [
                {"name": "urbanhacker.net (web)",
                    "cmd": "curl -fsSL https://urbanhacker.net"},
                {"name": "failure example (web)",
                 "cmd": "curl -fsSL https://fail.urbanhacker.net"}
            ]
        },
        {
            # Special section to display a custom text.
            "title": "Custom Text Section",
            "type": "text",
            "desc": "You can use a custom section at any place for various reason like planned maintenance.<br /><ul><li>Maintenance on the data center</li><li>Rebooting main servers</li></ul>"
        },
        {
            "title": "External Network",
            "type": "tests",
            "tests": [
                {"name": "DNS server 8.8.8.8 (ping)",
                 "cmd": "ping 8.8.8.8"},
                {"name": "linux.com (web)",
                    "cmd": "curl -fsSl https://linux.com"},
                {"name": "github.com (web)",
                    "cmd": "curl -fsSl https://github.com"},
            ]
        }
    ]
}
