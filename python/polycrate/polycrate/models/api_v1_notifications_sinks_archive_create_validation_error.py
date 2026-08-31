from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_archive_create_annotations_error_component import (
        ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_archived_at_error_component import (
        ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_archived_error_component import (
        ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_archived_reason_error_component import (
        ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_config_error_component import (
        ApiV1NotificationsSinksArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_criticality_error_component import (
        ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_debug_mode_error_component import (
        ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_display_name_error_component import (
        ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_enabled_model_types_error_component import (
        ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_is_enabled_error_component import (
        ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_is_system_default_error_component import (
        ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_kind_error_component import (
        ApiV1NotificationsSinksArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_labels_error_component import (
        ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_name_error_component import (
        ApiV1NotificationsSinksArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_non_field_errors_error_component import (
        ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_platform_service_error_component import (
        ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_provider_error_component import (
        ApiV1NotificationsSinksArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_provider_id_error_component import (
        ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_provider_reference_error_component import (
        ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_reconciliation_enabled_error_component import (
        ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_sla_availability_error_component import (
        ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_sla_target_error_component import (
        ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_slo_availability_error_component import (
        ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_slo_target_error_component import (
        ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_target_availability_error_component import (
        ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_archive_create_tolerations_error_component import (
        ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksArchiveCreateValidationError")


@_attrs_define
class ApiV1NotificationsSinksArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent |
            ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent |
            ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent |
            ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent |
            ApiV1NotificationsSinksArchiveCreateConfigErrorComponent |
            ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent |
            ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent |
            ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent |
            ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent |
            ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent |
            ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent |
            ApiV1NotificationsSinksArchiveCreateKindErrorComponent |
            ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent |
            ApiV1NotificationsSinksArchiveCreateNameErrorComponent |
            ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent |
            ApiV1NotificationsSinksArchiveCreateProviderErrorComponent |
            ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent |
            ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent |
            ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent |
            ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent |
            ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent |
            ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent
        | ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent
        | ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent
        | ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent
        | ApiV1NotificationsSinksArchiveCreateConfigErrorComponent
        | ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent
        | ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent
        | ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent
        | ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent
        | ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent
        | ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent
        | ApiV1NotificationsSinksArchiveCreateKindErrorComponent
        | ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent
        | ApiV1NotificationsSinksArchiveCreateNameErrorComponent
        | ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent
        | ApiV1NotificationsSinksArchiveCreateProviderErrorComponent
        | ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent
        | ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent
        | ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent
        | ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent
        | ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent
        | ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_archive_create_annotations_error_component import (
            ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_at_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_reason_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_config_error_component import (
            ApiV1NotificationsSinksArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_criticality_error_component import (
            ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_debug_mode_error_component import (
            ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_display_name_error_component import (
            ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_is_enabled_error_component import (
            ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_is_system_default_error_component import (
            ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_kind_error_component import (
            ApiV1NotificationsSinksArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_labels_error_component import (
            ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_name_error_component import (
            ApiV1NotificationsSinksArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_platform_service_error_component import (
            ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_id_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_reference_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_sla_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_sla_target_error_component import (
            ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_slo_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_slo_target_error_component import (
            ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_target_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_tolerations_error_component import (
            ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent):
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
        from ..models.api_v1_notifications_sinks_archive_create_annotations_error_component import (
            ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_at_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_archived_reason_error_component import (
            ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_config_error_component import (
            ApiV1NotificationsSinksArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_criticality_error_component import (
            ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_debug_mode_error_component import (
            ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_display_name_error_component import (
            ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_enabled_model_types_error_component import (
            ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_is_enabled_error_component import (
            ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_is_system_default_error_component import (
            ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_kind_error_component import (
            ApiV1NotificationsSinksArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_labels_error_component import (
            ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_name_error_component import (
            ApiV1NotificationsSinksArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_platform_service_error_component import (
            ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_id_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_provider_reference_error_component import (
            ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_sla_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_sla_target_error_component import (
            ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_slo_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_slo_target_error_component import (
            ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_target_availability_error_component import (
            ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_archive_create_tolerations_error_component import (
            ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent
                | ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent
                | ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent
                | ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent
                | ApiV1NotificationsSinksArchiveCreateConfigErrorComponent
                | ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent
                | ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent
                | ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent
                | ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent
                | ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent
                | ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent
                | ApiV1NotificationsSinksArchiveCreateKindErrorComponent
                | ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent
                | ApiV1NotificationsSinksArchiveCreateNameErrorComponent
                | ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent
                | ApiV1NotificationsSinksArchiveCreateProviderErrorComponent
                | ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent
                | ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent
                | ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent
                | ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent
                | ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent
                | ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_0 = (
                        ApiV1NotificationsSinksArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_1 = (
                        ApiV1NotificationsSinksArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_2 = (
                        ApiV1NotificationsSinksArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_3 = (
                        ApiV1NotificationsSinksArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_4 = (
                        ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_5 = (
                        ApiV1NotificationsSinksArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_6 = (
                        ApiV1NotificationsSinksArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_7 = (
                        ApiV1NotificationsSinksArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_8 = (
                        ApiV1NotificationsSinksArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_9 = (
                        ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_10 = (
                        ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_11 = (
                        ApiV1NotificationsSinksArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_12 = (
                        ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_13 = (
                        ApiV1NotificationsSinksArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_14 = (
                        ApiV1NotificationsSinksArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_15 = (
                        ApiV1NotificationsSinksArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_16 = (
                        ApiV1NotificationsSinksArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_17 = (
                        ApiV1NotificationsSinksArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_18 = (
                        ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_19 = (
                        ApiV1NotificationsSinksArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_20 = (
                        ApiV1NotificationsSinksArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_21 = (
                        ApiV1NotificationsSinksArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_22 = (
                        ApiV1NotificationsSinksArchiveCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_23 = (
                        ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_archive_create_error_type_24 = (
                        ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_archive_create_error_type_25 = (
                    ApiV1NotificationsSinksArchiveCreateEnabledModelTypesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_archive_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_archive_create_validation_error.additional_properties = d
        return api_v1_notifications_sinks_archive_create_validation_error

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
