# SqueakyDeaky

Ultrasonic sensor distance - annoys the dog

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<squeaky> *
  * Triggers a request for the distance of the ultrasonic sensor

**Outputs**

* \<deaky> "\<value>"
  * Returns the current distance reported by the ultrasonic sensor
  * Only in response to an input trigger