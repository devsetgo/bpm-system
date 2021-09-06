from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.decision_requirements_definition_dto import DecisionRequirementsDefinitionDto

T = TypeVar("T", bound="DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions")


@attr.s(auto_attribs=True)
class DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions:
    """A JSON Object containing a property for each of the decision requirements definitions,
    which are successfully deployed with that deployment.
    The key is the decision requirements definition id, the value is a JSON Object corresponding to the decision requirements definition."""

    additional_properties: Dict[str, DecisionRequirementsDefinitionDto] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deployment_with_definitions_dto_deployed_decision_requirements_definitions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DecisionRequirementsDefinitionDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        deployment_with_definitions_dto_deployed_decision_requirements_definitions.additional_properties = (
            additional_properties
        )
        return deployment_with_definitions_dto_deployed_decision_requirements_definitions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DecisionRequirementsDefinitionDto:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DecisionRequirementsDefinitionDto) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
