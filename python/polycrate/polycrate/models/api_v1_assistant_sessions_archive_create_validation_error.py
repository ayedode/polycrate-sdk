from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_assistant_sessions_archive_create_annotations_error_component import (
        ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_archived_at_error_component import (
        ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_archived_error_component import (
        ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_archived_reason_error_component import (
        ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_criticality_error_component import (
        ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_debug_mode_error_component import (
        ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_display_name_error_component import (
        ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_kind_error_component import (
        ApiV1AssistantSessionsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_labels_error_component import (
        ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_name_error_component import (
        ApiV1AssistantSessionsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_non_field_errors_error_component import (
        ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_platform_service_error_component import (
        ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_provider_error_component import (
        ApiV1AssistantSessionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_provider_id_error_component import (
        ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_provider_reference_error_component import (
        ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_reconciliation_enabled_error_component import (
        ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_sla_availability_error_component import (
        ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_sla_target_error_component import (
        ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_slo_availability_error_component import (
        ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_slo_target_error_component import (
        ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_status_error_component import (
        ApiV1AssistantSessionsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_target_availability_error_component import (
        ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_tolerations_error_component import (
        ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_archive_create_workspace_id_error_component import (
        ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AssistantSessionsArchiveCreateValidationError")


@_attrs_define
class ApiV1AssistantSessionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent |
            ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent |
            ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent |
            ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent |
            ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent |
            ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent |
            ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent |
            ApiV1AssistantSessionsArchiveCreateKindErrorComponent | ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent
            | ApiV1AssistantSessionsArchiveCreateNameErrorComponent |
            ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent |
            ApiV1AssistantSessionsArchiveCreateProviderErrorComponent |
            ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent |
            ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent |
            ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent |
            ApiV1AssistantSessionsArchiveCreateStatusErrorComponent |
            ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent |
            ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent
        | ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent
        | ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent
        | ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent
        | ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent
        | ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent
        | ApiV1AssistantSessionsArchiveCreateKindErrorComponent
        | ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent
        | ApiV1AssistantSessionsArchiveCreateNameErrorComponent
        | ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1AssistantSessionsArchiveCreateProviderErrorComponent
        | ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent
        | ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent
        | ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent
        | ApiV1AssistantSessionsArchiveCreateStatusErrorComponent
        | ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent
        | ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_assistant_sessions_archive_create_annotations_error_component import (
            ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_at_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_reason_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_criticality_error_component import (
            ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_debug_mode_error_component import (
            ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_display_name_error_component import (
            ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_kind_error_component import (
            ApiV1AssistantSessionsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_labels_error_component import (
            ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_name_error_component import (
            ApiV1AssistantSessionsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_platform_service_error_component import (
            ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_id_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_reference_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_sla_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_sla_target_error_component import (
            ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_slo_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_slo_target_error_component import (
            ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_target_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_tolerations_error_component import (
            ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_workspace_id_error_component import (
            ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent):
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
        from ..models.api_v1_assistant_sessions_archive_create_annotations_error_component import (
            ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_at_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_archived_reason_error_component import (
            ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_criticality_error_component import (
            ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_debug_mode_error_component import (
            ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_display_name_error_component import (
            ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_kind_error_component import (
            ApiV1AssistantSessionsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_labels_error_component import (
            ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_name_error_component import (
            ApiV1AssistantSessionsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_platform_service_error_component import (
            ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_id_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_provider_reference_error_component import (
            ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_sla_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_sla_target_error_component import (
            ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_slo_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_slo_target_error_component import (
            ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_status_error_component import (
            ApiV1AssistantSessionsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_target_availability_error_component import (
            ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_tolerations_error_component import (
            ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_archive_create_workspace_id_error_component import (
            ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent
                | ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent
                | ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent
                | ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent
                | ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent
                | ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent
                | ApiV1AssistantSessionsArchiveCreateKindErrorComponent
                | ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent
                | ApiV1AssistantSessionsArchiveCreateNameErrorComponent
                | ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1AssistantSessionsArchiveCreateProviderErrorComponent
                | ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent
                | ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent
                | ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent
                | ApiV1AssistantSessionsArchiveCreateStatusErrorComponent
                | ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent
                | ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_0 = (
                        ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_1 = (
                        ApiV1AssistantSessionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_2 = (
                        ApiV1AssistantSessionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_3 = (
                        ApiV1AssistantSessionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_4 = (
                        ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_5 = (
                        ApiV1AssistantSessionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_6 = (
                        ApiV1AssistantSessionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_7 = (
                        ApiV1AssistantSessionsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_8 = (
                        ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_9 = (
                        ApiV1AssistantSessionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_10 = (
                        ApiV1AssistantSessionsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_11 = (
                        ApiV1AssistantSessionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_12 = (
                        ApiV1AssistantSessionsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_13 = (
                        ApiV1AssistantSessionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_14 = (
                        ApiV1AssistantSessionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_15 = (
                        ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_16 = (
                        ApiV1AssistantSessionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_17 = (
                        ApiV1AssistantSessionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_18 = (
                        ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_19 = (
                        ApiV1AssistantSessionsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_20 = (
                        ApiV1AssistantSessionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_21 = (
                        ApiV1AssistantSessionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_archive_create_error_type_22 = (
                        ApiV1AssistantSessionsArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_assistant_sessions_archive_create_error_type_23 = (
                    ApiV1AssistantSessionsArchiveCreateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_assistant_sessions_archive_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_assistant_sessions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_assistant_sessions_archive_create_validation_error.additional_properties = d
        return api_v1_assistant_sessions_archive_create_validation_error

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
