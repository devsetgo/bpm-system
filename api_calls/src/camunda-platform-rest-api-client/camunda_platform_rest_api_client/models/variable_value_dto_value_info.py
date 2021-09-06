from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VariableValueDtoValueInfo")


@attr.s(auto_attribs=True)
class VariableValueDtoValueInfo:
    """A JSON object containing additional, value-type-dependent properties.
    For serialized variables of type Object, the following properties can be provided:

    * `objectTypeName`: A string representation of the object's type name.
    * `serializationDataFormat`: The serialization format used to store the variable.

    For serialized variables of type File, the following properties can be provided:

    * `filename`: The name of the file. This is not the variable name but the name that will be used when downloading the file again.
    * `mimetype`: The MIME type of the file that is being uploaded.
    * `encoding`: The encoding of the file that is being uploaded.

    The following property can be provided for all value types:

    * `transient`: Indicates whether the variable should be transient or
    not. See [documentation](https://docs.camunda.org/manual/7.15/user-guide/process-engine/variables#transient-variables) for more informations.
    (Not applicable for `decision-definition` and ` /process-instance/variables-async` endpoints)"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variable_value_dto_value_info = cls()

        variable_value_dto_value_info.additional_properties = d
        return variable_value_dto_value_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
