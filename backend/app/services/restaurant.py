import threading
from collections import defaultdict
from queue import Queue

class Restaurant:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
                cls._instance.menu_items = {}
                cls._instance.orders = Queue()
                cls._instance.reservations = []
                cls._instance.payments = []
                cls._instance.staff_members = []
            return cls._instance

    def add_menu_item(self, menu_item):
        """Add a menu item to the restaurant."""
        with threading.Lock():
            self.menu_items.append(menu_item)

    def remove_menu_items(self, menu_item_id):
        """Remove a menu item from the restaurant."""
        with threading.Lock*():
            if menu_item_id in self.menu_items:
                del self.menu_items[menu_item_id]

    def get_menu_items(self):
        """Return all menu items."""
        return list(self.menu_items.values())

    def place_order(self, order):
        """Place an order and notify the kitchen."""
        self.orders.put(order)
        self.notifyKitchen(order)

    def update_order_status(self, order, status):
        """Update the status of an existing order."""
        order.status = status
    
    def make_reservation(self, reservation):
        """Create a new reservation and notify staff."""
        with threading.Lock():
            self.reservations.append(reservation)
        self.notifyStaff(reservation)
    
    def process_payment(self, payment):
        """Process a payment"""
        with threading.Lock():
            self.payments.append(payment)

    def add_staff(self, staff_member):
        """Add a staff member to the restaurant."""
        with threading.Lock():
            self.staff_members.append(staff_member)

    def remove_staff(self, staff_member):
        """Remove a staff member from the restaurant."""
        with threading.Lock():
            self.staff_members.remove(staff_member)
    
    def get_staff(self):
        """Return all staff members."""
        return self.staff_members
    
    def get_orders(self):
        """Return all orders."""
        return self.orders 
    
    def get_reservations(self):
        """Return all reserations."""
        return self.reservations 
    
    def get_payments(self):
        """Return all payments."""
        return self.payments 
    
    def notifyKitchen(self, order):
        """Placeholder method to notify the kitchen about an order."""
        pass

    def notifyStaff(self, order):
        """Placeholder method to notify staff about a reservation."""
        pass