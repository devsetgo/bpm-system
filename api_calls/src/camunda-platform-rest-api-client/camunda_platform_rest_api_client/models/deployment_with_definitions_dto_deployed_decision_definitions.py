from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.decision_definition_dto import DecisionDefinitionDto

T = TypeVar("T", bound="DeploymentWithDefinitionsDtoDeployedDecisionDefinitions")


@attr.s(auto_attribs=True)
class DeploymentWithDefinitionsDtoDeployedDecisionDefinitions:
    """A JSON Object containing a property for each of the decision definitions,
    which are successfully deployed with that deployment.
    The key is the decision definition id, the value is a JSON Object corresponding to the decision definition."""

    additional_properties: Dict[str, DecisionDefinitionDto] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deployment_with_definitions_dto_deployed_decision_definitions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DecisionDefinitionDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        deployment_with_definitions_dto_deployed_decision_definitions.additional_properties = additional_properties
        return deployment_with_definitions_dto_deployed_decision_definitions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DecisionDefinitionDto:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DecisionDefinitionDto) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
