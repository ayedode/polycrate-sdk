from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_assistant_sessions_create_annotations_error_component import (
        ApiV1AssistantSessionsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_archived_at_error_component import (
        ApiV1AssistantSessionsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_archived_error_component import (
        ApiV1AssistantSessionsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_archived_reason_error_component import (
        ApiV1AssistantSessionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_criticality_error_component import (
        ApiV1AssistantSessionsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_debug_mode_error_component import (
        ApiV1AssistantSessionsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_display_name_error_component import (
        ApiV1AssistantSessionsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_kind_error_component import (
        ApiV1AssistantSessionsCreateKindErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_labels_error_component import (
        ApiV1AssistantSessionsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_name_error_component import (
        ApiV1AssistantSessionsCreateNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_non_field_errors_error_component import (
        ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_platform_service_error_component import (
        ApiV1AssistantSessionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_provider_error_component import (
        ApiV1AssistantSessionsCreateProviderErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_provider_id_error_component import (
        ApiV1AssistantSessionsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_provider_reference_error_component import (
        ApiV1AssistantSessionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_reconciliation_enabled_error_component import (
        ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_sla_availability_error_component import (
        ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_sla_target_error_component import (
        ApiV1AssistantSessionsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_slo_availability_error_component import (
        ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_slo_target_error_component import (
        ApiV1AssistantSessionsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_status_error_component import (
        ApiV1AssistantSessionsCreateStatusErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_target_availability_error_component import (
        ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_tolerations_error_component import (
        ApiV1AssistantSessionsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_create_workspace_id_error_component import (
        ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AssistantSessionsCreateValidationError")


@_attrs_define
class ApiV1AssistantSessionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AssistantSessionsCreateAnnotationsErrorComponent |
            ApiV1AssistantSessionsCreateArchivedAtErrorComponent | ApiV1AssistantSessionsCreateArchivedErrorComponent |
            ApiV1AssistantSessionsCreateArchivedReasonErrorComponent | ApiV1AssistantSessionsCreateCriticalityErrorComponent
            | ApiV1AssistantSessionsCreateDebugModeErrorComponent | ApiV1AssistantSessionsCreateDisplayNameErrorComponent |
            ApiV1AssistantSessionsCreateKindErrorComponent | ApiV1AssistantSessionsCreateLabelsErrorComponent |
            ApiV1AssistantSessionsCreateNameErrorComponent | ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent |
            ApiV1AssistantSessionsCreatePlatformServiceErrorComponent | ApiV1AssistantSessionsCreateProviderErrorComponent |
            ApiV1AssistantSessionsCreateProviderIdErrorComponent |
            ApiV1AssistantSessionsCreateProviderReferenceErrorComponent |
            ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent |
            ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent | ApiV1AssistantSessionsCreateSlaTargetErrorComponent
            | ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent |
            ApiV1AssistantSessionsCreateSloTargetErrorComponent | ApiV1AssistantSessionsCreateStatusErrorComponent |
            ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent |
            ApiV1AssistantSessionsCreateTolerationsErrorComponent | ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AssistantSessionsCreateAnnotationsErrorComponent
        | ApiV1AssistantSessionsCreateArchivedAtErrorComponent
        | ApiV1AssistantSessionsCreateArchivedErrorComponent
        | ApiV1AssistantSessionsCreateArchivedReasonErrorComponent
        | ApiV1AssistantSessionsCreateCriticalityErrorComponent
        | ApiV1AssistantSessionsCreateDebugModeErrorComponent
        | ApiV1AssistantSessionsCreateDisplayNameErrorComponent
        | ApiV1AssistantSessionsCreateKindErrorComponent
        | ApiV1AssistantSessionsCreateLabelsErrorComponent
        | ApiV1AssistantSessionsCreateNameErrorComponent
        | ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent
        | ApiV1AssistantSessionsCreatePlatformServiceErrorComponent
        | ApiV1AssistantSessionsCreateProviderErrorComponent
        | ApiV1AssistantSessionsCreateProviderIdErrorComponent
        | ApiV1AssistantSessionsCreateProviderReferenceErrorComponent
        | ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent
        | ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent
        | ApiV1AssistantSessionsCreateSlaTargetErrorComponent
        | ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent
        | ApiV1AssistantSessionsCreateSloTargetErrorComponent
        | ApiV1AssistantSessionsCreateStatusErrorComponent
        | ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent
        | ApiV1AssistantSessionsCreateTolerationsErrorComponent
        | ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_assistant_sessions_create_annotations_error_component import (
            ApiV1AssistantSessionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_at_error_component import (
            ApiV1AssistantSessionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_error_component import (
            ApiV1AssistantSessionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_reason_error_component import (
            ApiV1AssistantSessionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_criticality_error_component import (
            ApiV1AssistantSessionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_debug_mode_error_component import (
            ApiV1AssistantSessionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_display_name_error_component import (
            ApiV1AssistantSessionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_kind_error_component import (
            ApiV1AssistantSessionsCreateKindErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_labels_error_component import (
            ApiV1AssistantSessionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_name_error_component import (
            ApiV1AssistantSessionsCreateNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_platform_service_error_component import (
            ApiV1AssistantSessionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_error_component import (
            ApiV1AssistantSessionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_id_error_component import (
            ApiV1AssistantSessionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_reference_error_component import (
            ApiV1AssistantSessionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_sla_availability_error_component import (
            ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_sla_target_error_component import (
            ApiV1AssistantSessionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_slo_availability_error_component import (
            ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_slo_target_error_component import (
            ApiV1AssistantSessionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_target_availability_error_component import (
            ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_tolerations_error_component import (
            ApiV1AssistantSessionsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_workspace_id_error_component import (
            ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_assistant_sessions_create_annotations_error_component import (
            ApiV1AssistantSessionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_at_error_component import (
            ApiV1AssistantSessionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_error_component import (
            ApiV1AssistantSessionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_archived_reason_error_component import (
            ApiV1AssistantSessionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_criticality_error_component import (
            ApiV1AssistantSessionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_debug_mode_error_component import (
            ApiV1AssistantSessionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_display_name_error_component import (
            ApiV1AssistantSessionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_kind_error_component import (
            ApiV1AssistantSessionsCreateKindErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_labels_error_component import (
            ApiV1AssistantSessionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_name_error_component import (
            ApiV1AssistantSessionsCreateNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_platform_service_error_component import (
            ApiV1AssistantSessionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_error_component import (
            ApiV1AssistantSessionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_id_error_component import (
            ApiV1AssistantSessionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_provider_reference_error_component import (
            ApiV1AssistantSessionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_sla_availability_error_component import (
            ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_sla_target_error_component import (
            ApiV1AssistantSessionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_slo_availability_error_component import (
            ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_slo_target_error_component import (
            ApiV1AssistantSessionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_status_error_component import (
            ApiV1AssistantSessionsCreateStatusErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_target_availability_error_component import (
            ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_tolerations_error_component import (
            ApiV1AssistantSessionsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_create_workspace_id_error_component import (
            ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AssistantSessionsCreateAnnotationsErrorComponent
                | ApiV1AssistantSessionsCreateArchivedAtErrorComponent
                | ApiV1AssistantSessionsCreateArchivedErrorComponent
                | ApiV1AssistantSessionsCreateArchivedReasonErrorComponent
                | ApiV1AssistantSessionsCreateCriticalityErrorComponent
                | ApiV1AssistantSessionsCreateDebugModeErrorComponent
                | ApiV1AssistantSessionsCreateDisplayNameErrorComponent
                | ApiV1AssistantSessionsCreateKindErrorComponent
                | ApiV1AssistantSessionsCreateLabelsErrorComponent
                | ApiV1AssistantSessionsCreateNameErrorComponent
                | ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent
                | ApiV1AssistantSessionsCreatePlatformServiceErrorComponent
                | ApiV1AssistantSessionsCreateProviderErrorComponent
                | ApiV1AssistantSessionsCreateProviderIdErrorComponent
                | ApiV1AssistantSessionsCreateProviderReferenceErrorComponent
                | ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent
                | ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent
                | ApiV1AssistantSessionsCreateSlaTargetErrorComponent
                | ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent
                | ApiV1AssistantSessionsCreateSloTargetErrorComponent
                | ApiV1AssistantSessionsCreateStatusErrorComponent
                | ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent
                | ApiV1AssistantSessionsCreateTolerationsErrorComponent
                | ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_0 = (
                        ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_1 = (
                        ApiV1AssistantSessionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_2 = (
                        ApiV1AssistantSessionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_3 = (
                        ApiV1AssistantSessionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_4 = (
                        ApiV1AssistantSessionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_5 = (
                        ApiV1AssistantSessionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_6 = (
                        ApiV1AssistantSessionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_7 = (
                        ApiV1AssistantSessionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_8 = (
                        ApiV1AssistantSessionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_9 = (
                        ApiV1AssistantSessionsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_10 = (
                        ApiV1AssistantSessionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_11 = (
                        ApiV1AssistantSessionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_12 = (
                        ApiV1AssistantSessionsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_13 = (
                        ApiV1AssistantSessionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_14 = (
                        ApiV1AssistantSessionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_15 = (
                        ApiV1AssistantSessionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_16 = (
                        ApiV1AssistantSessionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_17 = (
                        ApiV1AssistantSessionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_18 = (
                        ApiV1AssistantSessionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_19 = (
                        ApiV1AssistantSessionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_20 = (
                        ApiV1AssistantSessionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_21 = (
                        ApiV1AssistantSessionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_create_error_type_22 = (
                        ApiV1AssistantSessionsCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_assistant_sessions_create_error_type_23 = (
                    ApiV1AssistantSessionsCreateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_assistant_sessions_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_assistant_sessions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_assistant_sessions_create_validation_error.additional_properties = d
        return api_v1_assistant_sessions_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
