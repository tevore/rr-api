package com.tevore.rrapi.domain;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Property;
import org.springframework.data.neo4j.core.schema.Relationship;

import java.util.List;

@Node("Event")
@Getter
@Setter
@ToString
public class Event {

    @Id
    @JsonIgnore
    private Long id;

    @Property("name")
    @JsonIgnore
    private String name;

    @Property("year")
    private Integer year;

    @Relationship(type = "WON", direction = Relationship.Direction.INCOMING)
    @JsonIgnore
    private List<Wrestler> winners;

    @JsonIgnore
    private List<Wrestler> participants;

    public Event(String name, Integer year) {
        this.name = name;
        this.year = year;
    }


}
