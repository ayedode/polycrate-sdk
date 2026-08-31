from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_assistant_sessions_update_annotations_error_component import (
        ApiV1AssistantSessionsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_archived_at_error_component import (
        ApiV1AssistantSessionsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_archived_error_component import (
        ApiV1AssistantSessionsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_archived_reason_error_component import (
        ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_criticality_error_component import (
        ApiV1AssistantSessionsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_debug_mode_error_component import (
        ApiV1AssistantSessionsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_display_name_error_component import (
        ApiV1AssistantSessionsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_kind_error_component import (
        ApiV1AssistantSessionsUpdateKindErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_labels_error_component import (
        ApiV1AssistantSessionsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_name_error_component import (
        ApiV1AssistantSessionsUpdateNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_non_field_errors_error_component import (
        ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_platform_service_error_component import (
        ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_provider_error_component import (
        ApiV1AssistantSessionsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_provider_id_error_component import (
        ApiV1AssistantSessionsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_provider_reference_error_component import (
        ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_reconciliation_enabled_error_component import (
        ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_sla_availability_error_component import (
        ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_sla_target_error_component import (
        ApiV1AssistantSessionsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_slo_availability_error_component import (
        ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_slo_target_error_component import (
        ApiV1AssistantSessionsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_status_error_component import (
        ApiV1AssistantSessionsUpdateStatusErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_target_availability_error_component import (
        ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_tolerations_error_component import (
        ApiV1AssistantSessionsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_update_workspace_id_error_component import (
        ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AssistantSessionsUpdateValidationError")


@_attrs_define
class ApiV1AssistantSessionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AssistantSessionsUpdateAnnotationsErrorComponent |
            ApiV1AssistantSessionsUpdateArchivedAtErrorComponent | ApiV1AssistantSessionsUpdateArchivedErrorComponent |
            ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent | ApiV1AssistantSessionsUpdateCriticalityErrorComponent
            | ApiV1AssistantSessionsUpdateDebugModeErrorComponent | ApiV1AssistantSessionsUpdateDisplayNameErrorComponent |
            ApiV1AssistantSessionsUpdateKindErrorComponent | ApiV1AssistantSessionsUpdateLabelsErrorComponent |
            ApiV1AssistantSessionsUpdateNameErrorComponent | ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent |
            ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent | ApiV1AssistantSessionsUpdateProviderErrorComponent |
            ApiV1AssistantSessionsUpdateProviderIdErrorComponent |
            ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent |
            ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent |
            ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent | ApiV1AssistantSessionsUpdateSlaTargetErrorComponent
            | ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent |
            ApiV1AssistantSessionsUpdateSloTargetErrorComponent | ApiV1AssistantSessionsUpdateStatusErrorComponent |
            ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent |
            ApiV1AssistantSessionsUpdateTolerationsErrorComponent | ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AssistantSessionsUpdateAnnotationsErrorComponent
        | ApiV1AssistantSessionsUpdateArchivedAtErrorComponent
        | ApiV1AssistantSessionsUpdateArchivedErrorComponent
        | ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent
        | ApiV1AssistantSessionsUpdateCriticalityErrorComponent
        | ApiV1AssistantSessionsUpdateDebugModeErrorComponent
        | ApiV1AssistantSessionsUpdateDisplayNameErrorComponent
        | ApiV1AssistantSessionsUpdateKindErrorComponent
        | ApiV1AssistantSessionsUpdateLabelsErrorComponent
        | ApiV1AssistantSessionsUpdateNameErrorComponent
        | ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent
        | ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent
        | ApiV1AssistantSessionsUpdateProviderErrorComponent
        | ApiV1AssistantSessionsUpdateProviderIdErrorComponent
        | ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent
        | ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent
        | ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent
        | ApiV1AssistantSessionsUpdateSlaTargetErrorComponent
        | ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent
        | ApiV1AssistantSessionsUpdateSloTargetErrorComponent
        | ApiV1AssistantSessionsUpdateStatusErrorComponent
        | ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent
        | ApiV1AssistantSessionsUpdateTolerationsErrorComponent
        | ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_assistant_sessions_update_annotations_error_component import (
            ApiV1AssistantSessionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_at_error_component import (
            ApiV1AssistantSessionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_error_component import (
            ApiV1AssistantSessionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_reason_error_component import (
            ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_criticality_error_component import (
            ApiV1AssistantSessionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_debug_mode_error_component import (
            ApiV1AssistantSessionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_display_name_error_component import (
            ApiV1AssistantSessionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_kind_error_component import (
            ApiV1AssistantSessionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_labels_error_component import (
            ApiV1AssistantSessionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_name_error_component import (
            ApiV1AssistantSessionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_non_field_errors_error_component import (
            ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_platform_service_error_component import (
            ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_error_component import (
            ApiV1AssistantSessionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_id_error_component import (
            ApiV1AssistantSessionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_reference_error_component import (
            ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_sla_availability_error_component import (
            ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_sla_target_error_component import (
            ApiV1AssistantSessionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_slo_availability_error_component import (
            ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_slo_target_error_component import (
            ApiV1AssistantSessionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_target_availability_error_component import (
            ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_tolerations_error_component import (
            ApiV1AssistantSessionsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_workspace_id_error_component import (
            ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent):
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
        from ..models.api_v1_assistant_sessions_update_annotations_error_component import (
            ApiV1AssistantSessionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_at_error_component import (
            ApiV1AssistantSessionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_error_component import (
            ApiV1AssistantSessionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_archived_reason_error_component import (
            ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_criticality_error_component import (
            ApiV1AssistantSessionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_debug_mode_error_component import (
            ApiV1AssistantSessionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_display_name_error_component import (
            ApiV1AssistantSessionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_kind_error_component import (
            ApiV1AssistantSessionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_labels_error_component import (
            ApiV1AssistantSessionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_name_error_component import (
            ApiV1AssistantSessionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_non_field_errors_error_component import (
            ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_platform_service_error_component import (
            ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_error_component import (
            ApiV1AssistantSessionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_id_error_component import (
            ApiV1AssistantSessionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_provider_reference_error_component import (
            ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_sla_availability_error_component import (
            ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_sla_target_error_component import (
            ApiV1AssistantSessionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_slo_availability_error_component import (
            ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_slo_target_error_component import (
            ApiV1AssistantSessionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_status_error_component import (
            ApiV1AssistantSessionsUpdateStatusErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_target_availability_error_component import (
            ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_tolerations_error_component import (
            ApiV1AssistantSessionsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_assistant_sessions_update_workspace_id_error_component import (
            ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AssistantSessionsUpdateAnnotationsErrorComponent
                | ApiV1AssistantSessionsUpdateArchivedAtErrorComponent
                | ApiV1AssistantSessionsUpdateArchivedErrorComponent
                | ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent
                | ApiV1AssistantSessionsUpdateCriticalityErrorComponent
                | ApiV1AssistantSessionsUpdateDebugModeErrorComponent
                | ApiV1AssistantSessionsUpdateDisplayNameErrorComponent
                | ApiV1AssistantSessionsUpdateKindErrorComponent
                | ApiV1AssistantSessionsUpdateLabelsErrorComponent
                | ApiV1AssistantSessionsUpdateNameErrorComponent
                | ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent
                | ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent
                | ApiV1AssistantSessionsUpdateProviderErrorComponent
                | ApiV1AssistantSessionsUpdateProviderIdErrorComponent
                | ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent
                | ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent
                | ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent
                | ApiV1AssistantSessionsUpdateSlaTargetErrorComponent
                | ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent
                | ApiV1AssistantSessionsUpdateSloTargetErrorComponent
                | ApiV1AssistantSessionsUpdateStatusErrorComponent
                | ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent
                | ApiV1AssistantSessionsUpdateTolerationsErrorComponent
                | ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_0 = (
                        ApiV1AssistantSessionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_1 = (
                        ApiV1AssistantSessionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_2 = (
                        ApiV1AssistantSessionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_3 = (
                        ApiV1AssistantSessionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_4 = (
                        ApiV1AssistantSessionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_5 = (
                        ApiV1AssistantSessionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_6 = (
                        ApiV1AssistantSessionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_7 = (
                        ApiV1AssistantSessionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_8 = (
                        ApiV1AssistantSessionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_9 = (
                        ApiV1AssistantSessionsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_10 = (
                        ApiV1AssistantSessionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_11 = (
                        ApiV1AssistantSessionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_12 = (
                        ApiV1AssistantSessionsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_13 = (
                        ApiV1AssistantSessionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_14 = (
                        ApiV1AssistantSessionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_15 = (
                        ApiV1AssistantSessionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_16 = (
                        ApiV1AssistantSessionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_17 = (
                        ApiV1AssistantSessionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_18 = (
                        ApiV1AssistantSessionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_19 = (
                        ApiV1AssistantSessionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_20 = (
                        ApiV1AssistantSessionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_21 = (
                        ApiV1AssistantSessionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_update_error_type_22 = (
                        ApiV1AssistantSessionsUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_assistant_sessions_update_error_type_23 = (
                    ApiV1AssistantSessionsUpdateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_assistant_sessions_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_assistant_sessions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_assistant_sessions_update_validation_error.additional_properties = d
        return api_v1_assistant_sessions_update_validation_error

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
