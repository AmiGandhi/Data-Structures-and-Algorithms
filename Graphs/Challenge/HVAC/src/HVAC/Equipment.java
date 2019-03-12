package HVAC;

public class Equipment {
    
    private String equipmentId;
    private Sensor sensor;
    
    public Equipment(String equipmentId, Sensor sensor ) {
        this.equipmentId = equipmentId;
        this.sensor =sensor;
    }
    
    public void setEquipmentId(String equipmentId) {
        this.equipmentId = equipmentId;
    }

    public String getEquipmentId() {
        return equipmentId;
    }

    public void setSensors(Sensor sensor) {
        this.sensor = sensor;
    }

    public Sensor getSensors() {
        return sensor;
    }
  
    
}
