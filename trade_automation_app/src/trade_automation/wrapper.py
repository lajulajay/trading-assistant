import sys
import os

# (Debugging: print sys.path before inserting the project root.)
print("sys.path (before insert):", sys.path)

# Insert the project root (i.e. the parent of trade_automation_app) so that etrade_client is importable.
# (Using a hardcoded absolute path as a workaround.)
sys.path.insert(0, "/Users/lajulajay/Developer/Etrade")

# (Debugging: print sys.path after inserting the project root.)
print("sys.path (after insert):", sys.path)

# (Debugging: print the absolute path of etrade_client (if it exists) so that we can verify that etrade_client is installed (and installed editable) in your venv.)
try:
    import etrade_client
    print("etrade_client.__file__:", etrade_client.__file__)
except ImportError as e:
    print("etrade_client import error:", e)

# (Debugging: print the absolute path of the wrapper (__file__) so that we can verify that the wrapper is being used.)
print("wrapper.__file__:", __file__)

# (Debugging: print a debug message so that we can verify that the wrapper is being used (i.e. that “python –m trade_automation.wrapper” is running wrapper.py as __main__).)
print("Running wrapper (__main__)")

# (Debugging: print “wrapper.__name__” so that we can verify that “__name__” is “__main__” (i.e. that “if __name__ == "__main__”:” is True) so that “main()” (from trade_automation.main) is called.)
print("wrapper.__name__:", __name__)

from trade_automation.main import main

if __name__ == "__main__":
    main() 