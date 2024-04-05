package models;

public class ManageUtilityIncident {

    private int customerId;
    private String utilityType;
    private String incidentStatus;
    private String incidentDescription;
    private String generateIncident;

    public ManageUtilityIncident(int customerId, String utilityType, String incidentStatus, String incidentDescription, String generateIncident) {
        this.customerId = customerId;
        this.utilityType = utilityType;
        this.incidentStatus = incidentStatus;
        this.incidentDescription = incidentDescription;
        this.generateIncident = generateIncident;
    }

    public int getCustomerId() {
        return customerId;
    }

    public void setCustomerId(int customerId) {
        this.customerId = customerId;
    }

    public String getUtilityType() {
        return utilityType;
    }

    public void setUtilityType(String utilityType) {
        this.utilityType = utilityType;
    }

    public String getIncidentStatus() {
        return incidentStatus;
    }

    public void setIncidentStatus(String incidentStatus) {
        this.incidentStatus = incidentStatus;
    }

    public String getIncidentDescription() {
        return incidentDescription;
    }

    public void setIncidentDescription(String incidentDescription) {
        this.incidentDescription = incidentDescription;
    }

    public String getGenerateIncident() {
        return generateIncident;
    }

    public void setGenerateIncident(String generateIncident) {
        this.generateIncident = generateIncident;
    }

    @Override
    public String toString() {
        return "ManageUtilityIncident{" +
                "customerId=" + customerId +
                ", utilityType='" + utilityType + '\'' +
                ", incidentStatus='" + incidentStatus + '\'' +
                ", incidentDescription='" + incidentDescription + '\'' +
                ", generateIncident='" + generateIncident + '\'' +
                '}';
    }
}
