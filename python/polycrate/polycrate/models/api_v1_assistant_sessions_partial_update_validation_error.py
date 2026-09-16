from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_assistant_sessions_partial_update_annotations_error_component import (
        ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_archived_at_error_component import (
        ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_archived_error_component import (
        ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_archived_reason_error_component import (
        ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_criticality_error_component import (
        ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_debug_mode_error_component import (
        ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_display_name_error_component import (
        ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_kind_error_component import (
        ApiV1AssistantSessionsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_labels_error_component import (
        ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_name_error_component import (
        ApiV1AssistantSessionsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_non_field_errors_error_component import (
        ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_platform_service_error_component import (
        ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_provider_error_component import (
        ApiV1AssistantSessionsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_provider_id_error_component import (
        ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_provider_reference_error_component import (
        ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_reconciliation_enabled_error_component import (
        ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_sla_availability_error_component import (
        ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_sla_target_error_component import (
        ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_slo_availability_error_component import (
        ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_slo_target_error_component import (
        ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_status_error_component import (
        ApiV1AssistantSessionsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_target_availability_error_component import (
        ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_tolerations_error_component import (
        ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_partial_update_workspace_id_error_component import (
        ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AssistantSessionsPartialUpdateValidationError")


@_attrs_define
class ApiV1AssistantSessionsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent |
            ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent |
            ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent |
            ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent |
            ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent |
            ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent |
            ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent |
            ApiV1AssistantSessionsPartialUpdateKindErrorComponent | ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent
            | ApiV1AssistantSessionsPartialUpdateNameErrorComponent |
            ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent |
            ApiV1AssistantSessionsPartialUpdateProviderErrorComponent |
            ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent |
            ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent |
            ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent |
            ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent |
            ApiV1AssistantSessionsPartialUpdateStatusErrorComponent |
            ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent |
            ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent
        | ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent
        | ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent
        | ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent
        | ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent
        | ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent
        | ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent
        | ApiV1AssistantSessionsPartialUpdateKindErrorComponent
        | ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent
        | ApiV1AssistantSessionsPartialUpdateNameErrorComponent
        | ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent
        | ApiV1AssistantSessionsPartialUpdateProviderErrorComponent
        | ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent
        | ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent
        | ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent
        | ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent
        | ApiV1AssistantSessionsPartialUpdateStatusErrorComponent
        | ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent
        | ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_assistant_sessions_partial_update_annotations_error_component import (
            ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_at_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_reason_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_criticality_error_component import (
            ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_debug_mode_error_component import (
            ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_display_name_error_component import (
            ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_kind_error_component import (
            ApiV1AssistantSessionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_labels_error_component import (
            ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_name_error_component import (
            ApiV1AssistantSessionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_non_field_errors_error_component import (
            ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_platform_service_error_component import (
            ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_id_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_reference_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_sla_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_sla_target_error_component import (
            ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_slo_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_slo_target_error_component import (
            ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_target_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_tolerations_error_component import (
            ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_workspace_id_error_component import (
            ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent):
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
        from ..models.api_v1_assistant_sessions_partial_update_annotations_error_component import (
            ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_at_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_archived_reason_error_component import (
            ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_criticality_error_component import (
            ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_debug_mode_error_component import (
            ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_display_name_error_component import (
            ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_kind_error_component import (
            ApiV1AssistantSessionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_labels_error_component import (
            ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_name_error_component import (
            ApiV1AssistantSessionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_non_field_errors_error_component import (
            ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_platform_service_error_component import (
            ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_id_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_provider_reference_error_component import (
            ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_sla_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_sla_target_error_component import (
            ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_slo_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_slo_target_error_component import (
            ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_status_error_component import (
            ApiV1AssistantSessionsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_target_availability_error_component import (
            ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_tolerations_error_component import (
            ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_partial_update_workspace_id_error_component import (
            ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent
                | ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent
                | ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent
                | ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent
                | ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent
                | ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent
                | ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent
                | ApiV1AssistantSessionsPartialUpdateKindErrorComponent
                | ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent
                | ApiV1AssistantSessionsPartialUpdateNameErrorComponent
                | ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent
                | ApiV1AssistantSessionsPartialUpdateProviderErrorComponent
                | ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent
                | ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent
                | ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent
                | ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent
                | ApiV1AssistantSessionsPartialUpdateStatusErrorComponent
                | ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent
                | ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_0 = (
                        ApiV1AssistantSessionsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_1 = (
                        ApiV1AssistantSessionsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_2 = (
                        ApiV1AssistantSessionsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_3 = (
                        ApiV1AssistantSessionsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_4 = (
                        ApiV1AssistantSessionsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_5 = (
                        ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_6 = (
                        ApiV1AssistantSessionsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_7 = (
                        ApiV1AssistantSessionsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_8 = (
                        ApiV1AssistantSessionsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_9 = (
                        ApiV1AssistantSessionsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_10 = (
                        ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_11 = (
                        ApiV1AssistantSessionsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_12 = (
                        ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_13 = (
                        ApiV1AssistantSessionsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_14 = (
                        ApiV1AssistantSessionsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_15 = (
                        ApiV1AssistantSessionsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_16 = (
                        ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_17 = (
                        ApiV1AssistantSessionsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_18 = (
                        ApiV1AssistantSessionsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_19 = (
                        ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_20 = (
                        ApiV1AssistantSessionsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_21 = (
                        ApiV1AssistantSessionsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_partial_update_error_type_22 = (
                        ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_assistant_sessions_partial_update_error_type_23 = (
                    ApiV1AssistantSessionsPartialUpdateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_assistant_sessions_partial_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_assistant_sessions_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_assistant_sessions_partial_update_validation_error.additional_properties = d
        return api_v1_assistant_sessions_partial_update_validation_error

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
