# Billing Software

The Billing Software is a Python-based application designed to handle billing and invoicing tasks for small businesses and shops. It provides a user-friendly interface for creating and managing bills, keeping track of sales, and generating invoices for customers.

## Key Features

- Create and manage bills with detailed information such as item names, quantities, and prices.
- Calculate total amounts and generate invoices for customers.
- Track sales and view sales reports for specific time periods.
- Support for multiple users with login authentication and permissions.
- Interactive charts to visualize sales data and trends.

## Technologies Used

- Python programming language
- PyQt5 for the graphical user interface
- SQLite database for data storage
- Qt Charts for data visualization

## Installation

To run the Billing Software, make sure you have Python and PyQt5 installed. Clone the repository, create a virtual environment, and install the required packages from the `requirements.txt` file:

```
git clone https://github.com/yourusername/billing-software.git
cd billing-software
python -m venv venv
source venv/bin/activate (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
python main.py
```

After installing the packages, navigate to `enve\lib\site-packages\Custom_Widgets\Widgets.py` and open the `Widgets.py` file. Apply the following changes:

1. In the `Widgets.py` file, find the `checkButtonGroup` function and modify it as shown below:

```python
def checkButtonGroup(self):
    btn = self.sender()
    group = btn.group
    groupBtns = getattr(self, "group_btns_"+str(group))
    active = getattr(self, "group_active_"+str(group))
    notActive = getattr(self, "group_not_active_"+str(group))

    for x in groupBtns:
        if not x == btn:
            x.setStyleSheet(notActive)
            x.active = False
            x.setIcon(x.inactiveIcon)

    btn.setStyleSheet(active)
    btn.active = True

    btn.setIcon(btn.activeIcon)
```


2. Find this `if condition` in the `applyJsonStyle` function and change it to this:

```python
if "QPushButtonGroup" in data:
        grp_count = 0
        for group in data['QPushButtonGroup']:
            grp_count += 1
            for button_info in group["Buttons"]:
                button_name = button_info["Name"]
                button_icon_active = button_info["IconActive"]
                button_icon_inactive = button_info["IconInactive"]

                if hasattr(self.ui, button_name):
                    btn = getattr(self.ui, button_name)
                    btn.groupParent = self
                    btn.active = False

                    if not isinstance(btn, QtWidgets.QPushButton):
                        raise Exception("Error: " + button_name + " is not a QPushButton object.")
                        return

                    setattr(btn, "group", grp_count)

                    if not hasattr(self, "group_btns_" + str(grp_count)):
                        setattr(self, "group_btns_" + str(grp_count), [])

                    getattr(self, "group_btns_" + str(grp_count)).append(btn)

                    btn.clicked.connect(self.checkButtonGroup)

                    # Load the icons using QPixmap and set them as the button icons
                    btn_icon_active = QPixmap(button_icon_active)
                    btn_icon_inactive = QPixmap(button_icon_inactive)

                    # Set the active and inactive icons
                    if button_name == 'dashboard_btn':
                        btn.setIcon(QtGui.QIcon(btn_icon_active))
                    else:
                        btn.setIcon(QtGui.QIcon(btn_icon_inactive))
                    btn.activeIcon = QtGui.QIcon(btn_icon_active)
                    btn.inactiveIcon = QtGui.QIcon(btn_icon_inactive)

                else:
                    raise Exception("Error: Button named " + button_name + " was not found.")
                    return

            activeStyle = ""
            notActiveStyle = ""
            if "Style" in group:
                for style in group["Style"]:
                    if "Active" in style:
                        activeStyle = style['Active']
                    if "NotActive" in style:
                        notActiveStyle = style['NotActive']

            getattr(self, "group_btns_" + str(grp_count))[0].active = True
            setattr(self, "group_active_" + str(grp_count), activeStyle)
            setattr(self, "group_not_active_" + str(grp_count), notActiveStyle)
```
