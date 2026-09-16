from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conditions_archive_create_annotations_error_component import (
        ApiV1ConditionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_archived_at_error_component import (
        ApiV1ConditionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_archived_error_component import (
        ApiV1ConditionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_archived_reason_error_component import (
        ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_criticality_error_component import (
        ApiV1ConditionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_debug_mode_error_component import (
        ApiV1ConditionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_description_error_component import (
        ApiV1ConditionsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_display_name_error_component import (
        ApiV1ConditionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_is_system_error_component import (
        ApiV1ConditionsArchiveCreateIsSystemErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_kind_error_component import (
        ApiV1ConditionsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_labels_error_component import (
        ApiV1ConditionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_name_error_component import (
        ApiV1ConditionsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_non_field_errors_error_component import (
        ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_platform_service_error_component import (
        ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_provider_error_component import (
        ApiV1ConditionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_provider_id_error_component import (
        ApiV1ConditionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_provider_reference_error_component import (
        ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_reconciliation_enabled_error_component import (
        ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_severity_error_component import (
        ApiV1ConditionsArchiveCreateSeverityErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_sla_availability_error_component import (
        ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_sla_target_error_component import (
        ApiV1ConditionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_slo_availability_error_component import (
        ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_slo_target_error_component import (
        ApiV1ConditionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_target_availability_error_component import (
        ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_archive_create_tolerations_error_component import (
        ApiV1ConditionsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionsArchiveCreateValidationError")


@_attrs_define
class ApiV1ConditionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionsArchiveCreateAnnotationsErrorComponent |
            ApiV1ConditionsArchiveCreateArchivedAtErrorComponent | ApiV1ConditionsArchiveCreateArchivedErrorComponent |
            ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent | ApiV1ConditionsArchiveCreateCriticalityErrorComponent
            | ApiV1ConditionsArchiveCreateDebugModeErrorComponent | ApiV1ConditionsArchiveCreateDescriptionErrorComponent |
            ApiV1ConditionsArchiveCreateDisplayNameErrorComponent | ApiV1ConditionsArchiveCreateIsSystemErrorComponent |
            ApiV1ConditionsArchiveCreateKindErrorComponent | ApiV1ConditionsArchiveCreateLabelsErrorComponent |
            ApiV1ConditionsArchiveCreateNameErrorComponent | ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent | ApiV1ConditionsArchiveCreateProviderErrorComponent |
            ApiV1ConditionsArchiveCreateProviderIdErrorComponent |
            ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ConditionsArchiveCreateSeverityErrorComponent | ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ConditionsArchiveCreateSlaTargetErrorComponent | ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent
            | ApiV1ConditionsArchiveCreateSloTargetErrorComponent |
            ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ConditionsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionsArchiveCreateAnnotationsErrorComponent
        | ApiV1ConditionsArchiveCreateArchivedAtErrorComponent
        | ApiV1ConditionsArchiveCreateArchivedErrorComponent
        | ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1ConditionsArchiveCreateCriticalityErrorComponent
        | ApiV1ConditionsArchiveCreateDebugModeErrorComponent
        | ApiV1ConditionsArchiveCreateDescriptionErrorComponent
        | ApiV1ConditionsArchiveCreateDisplayNameErrorComponent
        | ApiV1ConditionsArchiveCreateIsSystemErrorComponent
        | ApiV1ConditionsArchiveCreateKindErrorComponent
        | ApiV1ConditionsArchiveCreateLabelsErrorComponent
        | ApiV1ConditionsArchiveCreateNameErrorComponent
        | ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1ConditionsArchiveCreateProviderErrorComponent
        | ApiV1ConditionsArchiveCreateProviderIdErrorComponent
        | ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ConditionsArchiveCreateSeverityErrorComponent
        | ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ConditionsArchiveCreateSlaTargetErrorComponent
        | ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ConditionsArchiveCreateSloTargetErrorComponent
        | ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ConditionsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conditions_archive_create_annotations_error_component import (
            ApiV1ConditionsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_at_error_component import (
            ApiV1ConditionsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_error_component import (
            ApiV1ConditionsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_reason_error_component import (
            ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_criticality_error_component import (
            ApiV1ConditionsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_debug_mode_error_component import (
            ApiV1ConditionsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_display_name_error_component import (
            ApiV1ConditionsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_is_system_error_component import (
            ApiV1ConditionsArchiveCreateIsSystemErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_kind_error_component import (
            ApiV1ConditionsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_labels_error_component import (
            ApiV1ConditionsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_name_error_component import (
            ApiV1ConditionsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_non_field_errors_error_component import (
            ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_platform_service_error_component import (
            ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_error_component import (
            ApiV1ConditionsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_id_error_component import (
            ApiV1ConditionsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_reference_error_component import (
            ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_reconciliation_enabled_error_component import (
            ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_severity_error_component import (
            ApiV1ConditionsArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_sla_availability_error_component import (
            ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_sla_target_error_component import (
            ApiV1ConditionsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_slo_availability_error_component import (
            ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_slo_target_error_component import (
            ApiV1ConditionsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_target_availability_error_component import (
            ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_tolerations_error_component import (
            ApiV1ConditionsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsArchiveCreateIsSystemErrorComponent):
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
        from ..models.api_v1_conditions_archive_create_annotations_error_component import (
            ApiV1ConditionsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_at_error_component import (
            ApiV1ConditionsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_error_component import (
            ApiV1ConditionsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_archived_reason_error_component import (
            ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_criticality_error_component import (
            ApiV1ConditionsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_debug_mode_error_component import (
            ApiV1ConditionsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_description_error_component import (
            ApiV1ConditionsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_display_name_error_component import (
            ApiV1ConditionsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_is_system_error_component import (
            ApiV1ConditionsArchiveCreateIsSystemErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_kind_error_component import (
            ApiV1ConditionsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_labels_error_component import (
            ApiV1ConditionsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_name_error_component import (
            ApiV1ConditionsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_non_field_errors_error_component import (
            ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_platform_service_error_component import (
            ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_error_component import (
            ApiV1ConditionsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_id_error_component import (
            ApiV1ConditionsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_provider_reference_error_component import (
            ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_reconciliation_enabled_error_component import (
            ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_severity_error_component import (
            ApiV1ConditionsArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_sla_availability_error_component import (
            ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_sla_target_error_component import (
            ApiV1ConditionsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_slo_availability_error_component import (
            ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_slo_target_error_component import (
            ApiV1ConditionsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_target_availability_error_component import (
            ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conditions_archive_create_tolerations_error_component import (
            ApiV1ConditionsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionsArchiveCreateAnnotationsErrorComponent
                | ApiV1ConditionsArchiveCreateArchivedAtErrorComponent
                | ApiV1ConditionsArchiveCreateArchivedErrorComponent
                | ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1ConditionsArchiveCreateCriticalityErrorComponent
                | ApiV1ConditionsArchiveCreateDebugModeErrorComponent
                | ApiV1ConditionsArchiveCreateDescriptionErrorComponent
                | ApiV1ConditionsArchiveCreateDisplayNameErrorComponent
                | ApiV1ConditionsArchiveCreateIsSystemErrorComponent
                | ApiV1ConditionsArchiveCreateKindErrorComponent
                | ApiV1ConditionsArchiveCreateLabelsErrorComponent
                | ApiV1ConditionsArchiveCreateNameErrorComponent
                | ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1ConditionsArchiveCreateProviderErrorComponent
                | ApiV1ConditionsArchiveCreateProviderIdErrorComponent
                | ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ConditionsArchiveCreateSeverityErrorComponent
                | ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ConditionsArchiveCreateSlaTargetErrorComponent
                | ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ConditionsArchiveCreateSloTargetErrorComponent
                | ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ConditionsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_0 = (
                        ApiV1ConditionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_1 = (
                        ApiV1ConditionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_2 = (
                        ApiV1ConditionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_3 = (
                        ApiV1ConditionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_4 = (
                        ApiV1ConditionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_5 = (
                        ApiV1ConditionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_6 = (
                        ApiV1ConditionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_7 = (
                        ApiV1ConditionsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_8 = (
                        ApiV1ConditionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_9 = (
                        ApiV1ConditionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_10 = (
                        ApiV1ConditionsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_11 = (
                        ApiV1ConditionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_12 = (
                        ApiV1ConditionsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_13 = (
                        ApiV1ConditionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_14 = (
                        ApiV1ConditionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_15 = (
                        ApiV1ConditionsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_16 = (
                        ApiV1ConditionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_17 = (
                        ApiV1ConditionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_18 = (
                        ApiV1ConditionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_19 = (
                        ApiV1ConditionsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_20 = (
                        ApiV1ConditionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_21 = (
                        ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_22 = (
                        ApiV1ConditionsArchiveCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_archive_create_error_type_23 = (
                        ApiV1ConditionsArchiveCreateIsSystemErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conditions_archive_create_error_type_24 = (
                    ApiV1ConditionsArchiveCreateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conditions_archive_create_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conditions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conditions_archive_create_validation_error.additional_properties = d
        return api_v1_conditions_archive_create_validation_error

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
