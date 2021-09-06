import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.task_dto_delegation_state import TaskDtoDelegationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskDto")


@attr.s(auto_attribs=True)
class TaskDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    owner: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    due: Union[Unset, None, datetime.datetime] = UNSET
    follow_up: Union[Unset, None, datetime.datetime] = UNSET
    delegation_state: Union[Unset, None, TaskDtoDelegationState] = UNSET
    description: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    parent_task_id: Union[Unset, None, str] = UNSET
    priority: Union[Unset, None, int] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    case_execution_id: Union[Unset, None, str] = UNSET
    case_definition_id: Union[Unset, None, str] = UNSET
    case_instance_id: Union[Unset, None, str] = UNSET
    task_definition_key: Union[Unset, None, str] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    form_key: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        assignee = self.assignee
        owner = self.owner
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        due: Union[Unset, None, str] = UNSET
        if not isinstance(self.due, Unset):
            due = self.due.isoformat() if self.due else None

        follow_up: Union[Unset, None, str] = UNSET
        if not isinstance(self.follow_up, Unset):
            follow_up = self.follow_up.isoformat() if self.follow_up else None

        delegation_state: Union[Unset, None, str] = UNSET
        if not isinstance(self.delegation_state, Unset):
            delegation_state = self.delegation_state.value if self.delegation_state else None

        description = self.description
        execution_id = self.execution_id
        parent_task_id = self.parent_task_id
        priority = self.priority
        process_definition_id = self.process_definition_id
        process_instance_id = self.process_instance_id
        case_execution_id = self.case_execution_id
        case_definition_id = self.case_definition_id
        case_instance_id = self.case_instance_id
        task_definition_key = self.task_definition_key
        suspended = self.suspended
        form_key = self.form_key
        tenant_id = self.tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if owner is not UNSET:
            field_dict["owner"] = owner
        if created is not UNSET:
            field_dict["created"] = created
        if due is not UNSET:
            field_dict["due"] = due
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if delegation_state is not UNSET:
            field_dict["delegationState"] = delegation_state
        if description is not UNSET:
            field_dict["description"] = description
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if case_execution_id is not UNSET:
            field_dict["caseExecutionId"] = case_execution_id
        if case_definition_id is not UNSET:
            field_dict["caseDefinitionId"] = case_definition_id
        if case_instance_id is not UNSET:
            field_dict["caseInstanceId"] = case_instance_id
        if task_definition_key is not UNSET:
            field_dict["taskDefinitionKey"] = task_definition_key
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if form_key is not UNSET:
            field_dict["formKey"] = form_key
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        assignee = d.pop("assignee", UNSET)

        owner = d.pop("owner", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _due = d.pop("due", UNSET)
        due: Union[Unset, None, datetime.datetime]
        if _due is None:
            due = None
        elif isinstance(_due, Unset):
            due = UNSET
        else:
            due = isoparse(_due)

        _follow_up = d.pop("followUp", UNSET)
        follow_up: Union[Unset, None, datetime.datetime]
        if _follow_up is None:
            follow_up = None
        elif isinstance(_follow_up, Unset):
            follow_up = UNSET
        else:
            follow_up = isoparse(_follow_up)

        _delegation_state = d.pop("delegationState", UNSET)
        delegation_state: Union[Unset, None, TaskDtoDelegationState]
        if _delegation_state is None:
            delegation_state = None
        elif isinstance(_delegation_state, Unset):
            delegation_state = UNSET
        else:
            delegation_state = TaskDtoDelegationState(_delegation_state)

        description = d.pop("description", UNSET)

        execution_id = d.pop("executionId", UNSET)

        parent_task_id = d.pop("parentTaskId", UNSET)

        priority = d.pop("priority", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        case_execution_id = d.pop("caseExecutionId", UNSET)

        case_definition_id = d.pop("caseDefinitionId", UNSET)

        case_instance_id = d.pop("caseInstanceId", UNSET)

        task_definition_key = d.pop("taskDefinitionKey", UNSET)

        suspended = d.pop("suspended", UNSET)

        form_key = d.pop("formKey", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        task_dto = cls(
            id=id,
            name=name,
            assignee=assignee,
            owner=owner,
            created=created,
            due=due,
            follow_up=follow_up,
            delegation_state=delegation_state,
            description=description,
            execution_id=execution_id,
            parent_task_id=parent_task_id,
            priority=priority,
            process_definition_id=process_definition_id,
            process_instance_id=process_instance_id,
            case_execution_id=case_execution_id,
            case_definition_id=case_definition_id,
            case_instance_id=case_instance_id,
            task_definition_key=task_definition_key,
            suspended=suspended,
            form_key=form_key,
            tenant_id=tenant_id,
        )

        task_dto.additional_properties = d
        return task_dto

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
