# Bon Eppétit - Serverless Food Delivery Service
## Project Summary

### Pitch
In response to the challenges faced by fancy city-center restaurants due to remote work and downsizing, Bon Eppétit aims to revolutionize food delivery. This project introduces a new food delivery service that leverages electric bike delivery riders for hyperlocal deliveries, focusing on speed, cost-effectiveness, and environmental friendliness.

### Plan
The objective is to build a technical solution that can start small, iterate rapidly, and scale to handle millions of deliveries across various cities overnight. The team sees the potential in serverless technologies due to their pay-as-you-go model, scalability, and ease of expansion across regions.
![](https://static.us-east-1.prod.workshops.aws/public/50ba7239-ade8-423c-9236-be127b9939d8/static/intro/food-delivery-process.png)

### Process
The high-level actions and order statuses in the food delivery process include:

- Customer finds a restaurant, provides their location, and requests a list of nearby restaurants.
- Customer picks a restaurant, selects items, and places an order (PLACED).
- Customer pays for the order.
- Bon Eppétit! sends the order to the restaurant.
- Restaurant acknowledges the order (ACKNOWLEDGED).
- Customer can cancel the order before the restaurant starts making it (CANCELLED).
- Cancelled orders initiate a refund.
- Restaurant prepares the food (IN-PROCESS).
- Restaurant notifies Bon Eppétit! that the food is being made.
- Bon Eppétit! notifies the customer that the food is READY for delivery.
- Delivery Rider picks up the food (OUT-FOR-DELIVERY).
- Bon Eppétit! streams the food location to the customer.
- The order is delivered to the customer (DELIVERED).

### Solution Architecture Components
The system consists of various components and patterns, as depicted in the system components and patterns diagram. - The architecture incorporates serverless technologies to demonstrate scalable and cost-effective solutions. - Notable features include real-time order tracking, order status updates, and a seamless process flow.
![](https://static.us-east-1.prod.workshops.aws/public/50ba7239-ade8-423c-9236-be127b9939d8/static/intro/workload_components.png)

### Out of Scope
- No UI: The focus is on API development, and curl will be used for testing endpoints.
- No user account creation process: User accounts are not covered in this module but may be addressed in future workshop modules based on demand.

## Getting Started
Before diving into the code, ensure that your environment is set up for building the Bon Eppétit food delivery service. Follow the provided documentation to understand the system's architecture and start implementing the serverless solution.

Let the coding commence and Bon Appétit! 🚀🍽️