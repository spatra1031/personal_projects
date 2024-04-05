package controllers;

import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class ManageUtilityIncident {

    private final StringProperty customerId;
    private final StringProperty utilityType;
    private final StringProperty incidentStatus;
    private final StringProperty incidentDescription;
    private final StringProperty generateIncident;

    public ManageUtilityIncident(String customerId, String utilityType, String incidentStatus, String incidentDescription, String generateIncident) {
        this.customerId = new SimpleStringProperty(customerId);
        this.utilityType = new SimpleStringProperty(utilityType);
        this.incidentStatus = new SimpleStringProperty(incidentStatus);
        this.incidentDescription = new SimpleStringProperty(incidentDescription);
        this.generateIncident = new SimpleStringProperty(generateIncident);
    }

    public String getCustomerId() {
        return customerId.get();
    }

    public StringProperty customerIdProperty() {
        return customerId;
    }

    public String getUtilityType() {
        return utilityType.get();
    }

    public StringProperty utilityTypeProperty() {
        return utilityType;
    }

    public String getIncidentStatus() {
        return incidentStatus.get();
    }

    public StringProperty incidentStatusProperty() {
        return incidentStatus;
    }

    public String getIncidentDescription() {
        return incidentDescription.get();
    }

    public StringProperty incidentDescriptionProperty() {
        return incidentDescription;
    }

    public String getGenerateIncident() {
        return generateIncident.get();
    }

    public StringProperty generateIncidentProperty() {
        return generateIncident;
    }
}
