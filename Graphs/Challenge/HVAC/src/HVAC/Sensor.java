package HVAC;

public class Sensor {
    
    float temperature;
    float pressure;
    boolean status;

    public Sensor(float temperature,float pressure,boolean status) {
      this.temperature = temperature;
      this.pressure = pressure;
      this.status=status;
    }
    
    public float getTemperature() {
        return temperature;
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }

    public float getPressure() {
        return pressure;
    }

    public void setPressure(float pressure) {
        this.pressure = pressure;
    }

    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
    
    @Override
    public String toString() { 
        return String.format("the temperature is: " + temperature + ", pressure: " + pressure + " and status: " + status); 
    } 
}
