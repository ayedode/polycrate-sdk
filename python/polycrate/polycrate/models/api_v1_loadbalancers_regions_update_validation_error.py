from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_regions_update_active_error_component import (
        ApiV1LoadbalancersRegionsUpdateActiveErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_annotations_error_component import (
        ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_archived_at_error_component import (
        ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_archived_error_component import (
        ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_archived_reason_error_component import (
        ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_criticality_error_component import (
        ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_debug_mode_error_component import (
        ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_description_error_component import (
        ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_display_name_error_component import (
        ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_external_traffic_policy_error_component import (
        ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_kind_error_component import (
        ApiV1LoadbalancersRegionsUpdateKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_labels_error_component import (
        ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_name_error_component import (
        ApiV1LoadbalancersRegionsUpdateNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_non_field_errors_error_component import (
        ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_platform_service_error_component import (
        ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_provider_error_component import (
        ApiV1LoadbalancersRegionsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_provider_id_error_component import (
        ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_provider_reference_error_component import (
        ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_reconciliation_enabled_error_component import (
        ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_region_config_error_component import (
        ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_region_name_error_component import (
        ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_sla_availability_error_component import (
        ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_sla_target_error_component import (
        ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_slo_availability_error_component import (
        ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_slo_target_error_component import (
        ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_slug_error_component import (
        ApiV1LoadbalancersRegionsUpdateSlugErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_update_target_availability_error_component import (
        ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersRegionsUpdateValidationError")


@_attrs_define
class ApiV1LoadbalancersRegionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersRegionsUpdateActiveErrorComponent |
            ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent |
            ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent | ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent
            | ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent |
            ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent |
            ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent |
            ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent |
            ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent |
            ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent |
            ApiV1LoadbalancersRegionsUpdateKindErrorComponent | ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent |
            ApiV1LoadbalancersRegionsUpdateNameErrorComponent | ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent
            | ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent |
            ApiV1LoadbalancersRegionsUpdateProviderErrorComponent | ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent
            | ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent |
            ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent |
            ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent |
            ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent |
            ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent |
            ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent | ApiV1LoadbalancersRegionsUpdateSlugErrorComponent |
            ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersRegionsUpdateActiveErrorComponent
        | ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent
        | ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent
        | ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent
        | ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent
        | ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent
        | ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent
        | ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent
        | ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent
        | ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent
        | ApiV1LoadbalancersRegionsUpdateKindErrorComponent
        | ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent
        | ApiV1LoadbalancersRegionsUpdateNameErrorComponent
        | ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent
        | ApiV1LoadbalancersRegionsUpdateProviderErrorComponent
        | ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent
        | ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent
        | ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent
        | ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent
        | ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent
        | ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent
        | ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent
        | ApiV1LoadbalancersRegionsUpdateSlugErrorComponent
        | ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_regions_update_active_error_component import (
            ApiV1LoadbalancersRegionsUpdateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_annotations_error_component import (
            ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_at_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_criticality_error_component import (
            ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_description_error_component import (
            ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_display_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_kind_error_component import (
            ApiV1LoadbalancersRegionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_labels_error_component import (
            ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_platform_service_error_component import (
            ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_id_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_region_config_error_component import (
            ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_region_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_sla_target_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slo_target_error_component import (
            ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slug_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_target_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent):
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
        from ..models.api_v1_loadbalancers_regions_update_active_error_component import (
            ApiV1LoadbalancersRegionsUpdateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_annotations_error_component import (
            ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_at_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_criticality_error_component import (
            ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_description_error_component import (
            ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_display_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_external_traffic_policy_error_component import (
            ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_kind_error_component import (
            ApiV1LoadbalancersRegionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_labels_error_component import (
            ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_platform_service_error_component import (
            ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_id_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_region_config_error_component import (
            ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_region_name_error_component import (
            ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_sla_target_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slo_target_error_component import (
            ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_slug_error_component import (
            ApiV1LoadbalancersRegionsUpdateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_update_target_availability_error_component import (
            ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersRegionsUpdateActiveErrorComponent
                | ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent
                | ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent
                | ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent
                | ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent
                | ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent
                | ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent
                | ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent
                | ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent
                | ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent
                | ApiV1LoadbalancersRegionsUpdateKindErrorComponent
                | ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent
                | ApiV1LoadbalancersRegionsUpdateNameErrorComponent
                | ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent
                | ApiV1LoadbalancersRegionsUpdateProviderErrorComponent
                | ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent
                | ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent
                | ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent
                | ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent
                | ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent
                | ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent
                | ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent
                | ApiV1LoadbalancersRegionsUpdateSlugErrorComponent
                | ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_0 = (
                        ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_1 = (
                        ApiV1LoadbalancersRegionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_2 = (
                        ApiV1LoadbalancersRegionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_3 = (
                        ApiV1LoadbalancersRegionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_4 = (
                        ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_5 = (
                        ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_6 = (
                        ApiV1LoadbalancersRegionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_7 = (
                        ApiV1LoadbalancersRegionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_8 = (
                        ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_9 = (
                        ApiV1LoadbalancersRegionsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_10 = (
                        ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_11 = (
                        ApiV1LoadbalancersRegionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_12 = (
                        ApiV1LoadbalancersRegionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_13 = (
                        ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_14 = (
                        ApiV1LoadbalancersRegionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_15 = (
                        ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_16 = (
                        ApiV1LoadbalancersRegionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_17 = (
                        ApiV1LoadbalancersRegionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_18 = (
                        ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_19 = (
                        ApiV1LoadbalancersRegionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_20 = (
                        ApiV1LoadbalancersRegionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_21 = (
                        ApiV1LoadbalancersRegionsUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_22 = (
                        ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_23 = (
                        ApiV1LoadbalancersRegionsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_24 = (
                        ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_update_error_type_25 = (
                        ApiV1LoadbalancersRegionsUpdateRegionConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_regions_update_error_type_26 = (
                    ApiV1LoadbalancersRegionsUpdateExternalTrafficPolicyErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_regions_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_regions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_regions_update_validation_error.additional_properties = d
        return api_v1_loadbalancers_regions_update_validation_error

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
