Duration: May 24, 2024, 11:45 GMT to May  25, 2024, 07:00 GMT

Impact: Users encountered slow page loading times and occcasional 503 errors. This affected about 30% of users, their website had intermitted outages.
Root cause: The load balancer settings were not configured properly leading to excessive connections to overload some frontend servers.

Timeline:
	11:45 GMT: The issue was detected through the errors in the frontend responses as well as monitoring alerts.
	12:00 GMT: Investigation took place in order to find the problem.Due to schema
	updates it was suspected that issue could be within the database.
	13:30 GMT: After countless attempts to solve an issue with the database engineers
	concluded that the database was working fine and they proceeded to start a brand
	new investigation.
	14:50 GMT: After monitoring the CDN performance engineers spotted unusual caching
	behavior.
	15:00 GMT: This incident was forworded to the Infrastructure Team for further
	diagnosis.
	15:25 GMT: The infrastructure team was sucessfully able to identify the
	problem within the load balancer settings.
	16:45 GMT: The load balancer settings were properly adjusted and traffic was
	redistributed evenly across the frontend servers.
	18:15 GMT: Service was restored fully latency returning to normal levels hence
	errors subsiding.
Root cause and Resolution:
Root cause explanation: A recent update of the load balancer configuration, this update meant to optimize traffic routing.Unfortunately this lead to certain frontend servers recieving a disproportionately high number of connections which resulted in low performance.
Resolution Details: In order to solve the problem, engineers pulled the recent config change on the load balancer.They also analyzed and adjusted load balancing algorithms to distribute traffic evenly across all open frontend servers.After this process the strain on the overloaded servers was eased therefore restoring normal service functionality.

Corrective and Preventative Measures:
Improvements:
	    Change the management procedures for complex infrastrature componente to minimize misconfigurations.
	    Enhance the monitoring capabilities so that it detects abnormalities in traffic 
	    patterns.
